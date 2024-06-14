from PySide6.QtCore import *
from PySide6.QtWidgets import *
from main_ui_file import *
from cali_ui_file import *
from VR_Tracker import*

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import time



class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.caliPop = CaliPopUp()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('images/main_app_icon.png'))
        self.setWindowTitle('Vive Ground Truth System')
        self.caliPop.setWindowTitle('Calibration')
        self.caliPop.setWindowIcon(QIcon('images/main_app_icon.png'))
        
        # Initialize the 3D plot
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111, projection='3d')
        self.plotxy_lim_min = -150
        self.plotxy_lim_max = 150
        self.plotz_lim_min = 0
        self.plotz_lim_max = 280
        self.plot_xLabel = "X"
        self.plot_yLabel = "Y"
        self.plot_zLabel = "Z"
        self.plot_tick_start = -150
        self.plot_tick_interval = 100
        self.plot_tick_max = 150

        plotFrameLayout = QVBoxLayout()
        self.ui.plotFrameContainer.setLayout(plotFrameLayout)
        plotFrameLayout.addWidget(self.canvas)  # Assuming there's a layout
        
        # Set Up Log Box and Model
        self.logModel = QStringListModel(self)
        self.ui.log_box.setModel(self.logModel)
        
        # Button Connections
        self.ui.homeButton.clicked.connect(self.HomeButtonClicked)
        self.ui.calibrationButton.clicked.connect(self.CalibrateButtonClicked)
        self.ui.trackingButton.clicked.connect(self.TrackingButtonClicked)
        self.ui.dataButton.clicked.connect(self.dataButtonClicked)
        self.ui.quitButton.clicked.connect(self.end_app)
        
        self.tracker = HTC_Tracker(log_fnc=self.add_log_message)
        
        # Loops
        self.timer1 = QTimer(self)
        self.timer1.setInterval(50)
        self.timer1.timeout.connect(self.loop1)
        self.timer1.start()
        
        self.timer2 = QTimer(self)
        self.timer2.setInterval(1000)
        self.timer2.timeout.connect(self.loop2)
        self.timer2.start()
        
        # self.tracker = HTC_Tracker(log_fnc=self.add_log_message)
        # self.tracker_i = self.tracker.get_device_index(openvr.TrackedDeviceClass_GenericTracker)
        
    def loop1(self):
        x = np.random.uniform(-150, 150)
        y = np.random.uniform(-150, 150)
        z = np.random.uniform(0, 280)
        self.updateX(x)
        self.updateY(y)
        self.updateZ(z)
        self.plot_multiple_points(x, y, z)
        
    def loop2(self):
        self.set_vr_connected(self.tracker.vr_active)
        
        
    def plot_single_point(self, x, y, z):
        """ Plot a single point in the 3D plot and clear previous ones """
        self.ax.clear()
        self.ax.scatter([x], [y], [z], color='b')
        self.ax.set_xlim([self.plotxy_lim_min, self.plotxy_lim_max])  # Adjust according to your data range
        self.ax.set_ylim([self.plotxy_lim_min, self.plotxy_lim_max])
        self.ax.set_zlim([self.plotz_lim_min, self.plotz_lim_max])
        
        self.ax.set_xticks(np.arange(self.plot_tick_start, self.plot_tick_max + 1, self.plot_tick_interval))
        self.ax.set_yticks(np.arange(self.plot_tick_start, self.plot_tick_max + 1, self.plot_tick_interval))
        
        self.ax.set_xlabel(self.plot_xLabel)
        self.ax.set_ylabel(self.plot_yLabel)
        self.ax.set_zlabel(self.plot_zLabel)
        self.canvas.draw()
        
    def plot_multiple_points(self, x, y, z):
        """ Add a point to the 3D plot without clearing previous ones """
        self.ax.scatter([x], [y], [z], color='r')
        self.ax.set_xlim([self.plotxy_lim_min, self.plotxy_lim_max])  # Adjust according to your data range
        self.ax.set_ylim([self.plotxy_lim_min, self.plotxy_lim_max])
        self.ax.set_zlim([self.plotz_lim_min, self.plotz_lim_max])
        self.ax.set_xlabel(self.plot_xLabel)
        self.ax.set_ylabel(self.plot_yLabel)
        self.ax.set_zlabel(self.plot_zLabel)
        self.canvas.draw()
        
    def updateX(self, x):
        self.ui.xValue.setText(str(x))
        
    def updateY(self, y):
        self.ui.yValue.setText(str(y))
        
    def updateZ(self, z):
        self.ui.zValue.setText(str(z))
        
    def HomeButtonClicked(self):
        self.add_log_message("Home Clicked")
        
    def CalibrateButtonClicked(self):
        self.caliPop.show()
        self.add_log_message("Cali Button Clicked")
        
    def TrackingButtonClicked(self):
        self.add_log_message("Track Button Clicked")
        self.set_vr_connected(0)
        
    def dataButtonClicked(self):
        self.add_log_message("Data Button Clicked")
        self.set_vr_connected(1)
        
    def set_vr_connected(self, bool):
        if bool == 1:
            self.ui.VRstatus_label.setStyleSheet(u"color: rgb(50, 255, 0)")
            self.ui.VRstatus_label.setText("VR Connected")
        else:
            self.ui.VRstatus_label.setStyleSheet(u"color: rgb(255, 0, 0)")
            self.ui.VRstatus_label.setText("VR Not Connected")
        
        
        
    def end_app(self):
        app.exit()
        
    def add_log_message(self, message=""):
        
        current_logs = self.logModel.stringList()
        current_logs.append(message)
        self.logModel.setStringList(current_logs)
        
        self.ui.log_box.scrollToBottom()

class CaliPopUp(QMainWindow):
    def __init__(self):
        super(CaliPopUp, self).__init__()
        self.ui = Ui_CalibrationWindow()
        self.ui.setupUi(self) 
        
        
app = QApplication([])
MainAppWin = MainApp()



def app_init():
    MainAppWin.show()
def app_test():
    pass
        
app_init()
app.exec()