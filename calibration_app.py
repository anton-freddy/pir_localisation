from PySide6.QtCore import *
from PySide6.QtWidgets import *
from CalibrationWindow_ui import *
from VR_Tracker import*
from settings_json import *

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.gridspec import GridSpec
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import time

class CaliWindowApp(QMainWindow):
    def __init__(self, main_app=None, log_fnc=None, settings_handler=JSONSettingsHandler('settings.json')):
        super(CaliWindowApp, self).__init__()
        self.ui = Ui_Calibration()
        self.ui.setupUi(self) 
        self.main_app = main_app
        self.log = log_fnc or self.default_log
        self.settings_handler = settings_handler
        
        # Intialize 3D plot
        self.figure = Figure()
        
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(211)
        self.plotxy_lim_min = -150
        self.plotxy_lim_max = 150
        self.plot_xLabel = "X"
        self.plot_yLabel = "Y"
        self.plot_tick_start = -150
        self.plot_tick_interval = 100
        self.plot_tick_max = 150
        self.figure.tight_layout(pad=5)
        self.y_coords = []
        self.x_coords = []
        self.point_index = 0
        self.point_states = []

        plotFrameLayout = QVBoxLayout()
        
        for i in range(plotFrameLayout.count()):
            item = plotFrameLayout.itemAt(i)
            if not isinstance(item.widget(), type(self.canvas)):  # Keep only the canvas
                if item.widget():
                    widget_to_remove = item.widget()
                    plotFrameLayout.removeWidget(widget_to_remove)
                    widget_to_remove.setParent(None)
                    widget_to_remove.deleteLater()
                elif item.spacerItem():
                    # Remove the spacer item if found
                    spacer_to_remove = item.spacerItem()
                    plotFrameLayout.removeItem(spacer_to_remove)



        plotFrameLayout.setContentsMargins(0,0,0,0)
        plotFrameLayout.setSpacing(0)
        self.ui.graphFrame.setLayout(plotFrameLayout)
        plotFrameLayout.addWidget(self.canvas)  # Assuming there's a layout
        plotFrameLayout.setContentsMargins(0,0,0,0)
        
        self.canvas.draw()
        self.ui.graphFrame.update()

        
        
        
        self.ui.abortButton.clicked.connect(self.close)
        self.ui.nextPointButton.clicked.connect(self.nextPointButtonPressed)
        self.ui.recordPointButton.clicked.connect(self.recordPoint)

        
    def close(self):
        self.destroy()
        
    def save_and_close(self):
        # Add code for saving 
        
        self.close()
    
    def default_log(self, message):
        print(message)
        
    def get_calibration_points(self):
        self.calibration_pos = self.settings_handler.get_setting(JSON_calibration_array)
        if self.calibration_pos:  # Check if there are any points to plot
            self.x_coords = [point[0] for point in self.calibration_pos]  # Extract x coordinates
            self.y_coords = [point[1] for point in self.calibration_pos]  # Extract y coordinates
            self.point_states = ['unrecorded' for _ in self.calibration_pos]
        
    def plot_calibration_points(self): 
        self.ax.clear()  # Clear previous points to redraw
        for i, (x, y) in enumerate(zip(self.x_coords, self.y_coords)):
            color = 'r'  # Default unrecorded points in red
            if self.point_states[i] == 'current':
                color = 'b'  # Current point in blue
            elif self.point_states[i] == 'recorded':
                color = 'g'  # Recorded points in green
            self.ax.scatter(x, y, color=color)
        self.ax.set_xticks(np.arange(self.plot_tick_start, self.plot_tick_max + 1, self.plot_tick_interval))
        self.ax.set_yticks(np.arange(self.plot_tick_start, self.plot_tick_max + 1, self.plot_tick_interval))
        self.ax.set_aspect('auto')
        self.canvas.draw()
    
    def on_start_up(self):
        self.get_calibration_points()
        self.point_states[0] = 'current'  # Set the first point as current
        self.plot_calibration_points()
        self.ui.currentPointValue.setText(str(self.point_index + 1))


    
    def nextPointButtonPressed(self):
        if self.point_index < len(self.x_coords):
            self.point_states[self.point_index] = 'recorded' if self.point_states[self.point_index] == 'current' else self.point_states[self.point_index]
            self.point_index += 1
            self.point_index %= len(self.x_coords)  # Wrap around to the start if it goes past the last index
            self.point_states[self.point_index] = 'current'
            self.plot_calibration_points()
            self.ui.currentPointValue.setText(str(self.point_index + 1))


    def recordPoint(self):
        if self.point_index < len(self.x_coords):
            self.point_states[self.point_index] = 'recorded'
            self.plot_calibration_points()
