from PySide6.QtCore import *
from PySide6.QtWidgets import *
from settings_ui import *
from VR_Tracker import*
from settings_json import *

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.gridspec import GridSpec
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import time

class SettingsWindowApp(QMainWindow):
    def __init__(self, main_app=None, log_fnc=None, settings_handler=JSONSettingsHandler('settings.json')):
        super(SettingsWindowApp, self).__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.main_app = main_app
        self.settings_handler = settings_handler
        self.log = log_fnc or self.default_log
        self.load_all_settings()
        
        self.ui.exit_button.clicked.connect(self.close)
        self.ui.save_and_exit_button.clicked.connect(self.save_and_exit)
        self.ui.save_button.clicked.connect(self.save_all_changes)
        
    def load_all_settings(self):
        self.load_cali_table()
        self.load_min_max()
        
    def save_all_changes(self):
        self.save_cali_table()
        self.save_min_max()
        self.main_app.caliWindow.on_start_up()
        
        
    def save_min_max(self):
        x_min_max = [float(self.ui.x_min.text()), float(self.ui.x_max.text())]
        y_min_max = [float(self.ui.y_min.text()), float(self.ui.y_max.text())]
        self.settings_handler.set_setting(JSON_x_min_max, x_min_max)
        self.settings_handler.set_setting(JSON_y_min_max, y_min_max)
    
    def load_min_max(self):
        x_min_max = self.settings_handler.get_setting(JSON_x_min_max)
        y_min_max = self.settings_handler.get_setting(JSON_y_min_max)
        
        if x_min_max and y_min_max:
            self.ui.x_min.setText(str(x_min_max[0]))
            self.ui.x_max.setText(str(x_min_max[1]))
            self.ui.y_min.setText(str(y_min_max[0]))
            self.ui.y_max.setText(str(y_min_max[1]))
        else:
            self.log("No settings found for min/max values. Please set up settings")
            self.ui.x_min.setText('Not Set')
            self.ui.x_max.setText('Not Set')
            self.ui.y_min.setText('Not Set')
            self.ui.y_max.setText('Not Set')
        
    def load_cali_table(self):
        cali_pos = self.settings_handler.get_setting(JSON_calibration_array)
        #self.ui.cali_points.setRowCount(0)  # Clear existing rows first
        if cali_pos:
            for row_index, pos in enumerate(cali_pos):
                for col_index, value in enumerate(pos):
                    self.ui.cali_points.setItem(row_index, col_index, QTableWidgetItem(str(value)))

        
    def save_cali_table(self):
        cali_pos = []
        for row_index in range(self.ui.cali_points.rowCount()):
            row_data = []
            for col_index in range(self.ui.cali_points.columnCount()):
                item = self.ui.cali_points.item(row_index, col_index)
                if item is not None and item.text().strip():
                    try:
                        value = float(item.text())
                    except ValueError:
                        self.log(f"Invalid input in row {row_index+1}, column {col_index+1}. Please enter a numeric value.")
                        return  # Stops saving if there's an error
                    row_data.append(value)
                else:
                    row_data.append(0.0)  # Default value or handle as error
            cali_pos.append(row_data)

        self.settings_handler.set_setting(JSON_calibration_array, cali_pos)
        
        
    def save_and_exit(self):
        self.save_all_changes()
        self.close()
        
    

    def default_log(self, message):
        print(message)
    
    def log(self, message):
        self.log(message)