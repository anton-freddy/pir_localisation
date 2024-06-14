from PySide6.QtCore import *
from PySide6.QtWidgets import *
from main_ui_file import *
from cali_ui_file import *
from VR_Tracker import*
import time



class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.caliPop = CaliPopUp()
        self.ui.setupUi(self)
        
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
        self.tracker_i = self.tracker.get_device_index(openvr.TrackedDeviceClass_GenericTracker)
        
    def updateX(self, x):
        self.ui.xValue.setText(x)
        
    def updateY(self, y):
        self.ui.yValue.setText(y)
        
    def updateZ(self, z):
        self.ui.zValue.setText(z)
        
    def HomeButtonClicked(self):
        self.ui.pagesWidget.setCurrentWidget(self.ui.HomePage)
        
    def CalibrateButtonClicked(self):
        self.caliPop.show()
        self.add_log_message("Cali Button Clicked")
        
    def TrackingButtonClicked(self):
        self.ui.pagesWidget.setCurrentWidget(self.ui.TrackingPage)
        self.add_log_message("Track Button Clicked")
        
    def dataButtonClicked(self):
        self.ui.pagesWidget.setCurrentWidget(self.ui.DataPage)
        self.add_log_message("Data Button Clicked")
        
        
        
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