import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
from implementation import implementation
imp = implementation()

class TrackerApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Tracker System Control")
        self.config_path = 'config.json'
        self.config = load_config(self.config_path)
        self.calibration_positions = [
            (100, -100), (100, 0), (100, 100),
            (0, -100), (0, 0), (0, 100),
            (-100, -100), (-100, 0), (-100, 100)
        ]
        self.calibration_index = 0
        self.calibration_measurements = []
        self.tracker_i = initialize_tracker()

        self.setup_gui()
        self.setup_plot()

    # GUI setup functions here (from original script)
    def setup_gui(self):
        # Tabs
        self.tab_control = ttk.Notebook(self.master)
        self.calibration_tab = ttk.Frame(self.tab_control)
        self.tracking_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.calibration_tab, text='Calibration')
        self.tab_control.add(self.tracking_tab, text='Tracking')
        self.tab_control.pack(expand=1, fill="both")

        # Calibration Tab
        self.calibration_label = ttk.Label(self.calibration_tab, text="Click 'Start Calibration' to begin.")
        self.calibration_label.pack(pady=10)

        self.calib_button = ttk.Button(self.calibration_tab, text="Start Calibration", command=self.start_calibration)
        self.calib_button.pack(pady=20)

        self.calib_next_button = ttk.Button(self.calibration_tab, text="Record Position", command=self.record_position)
        self.calib_next_button.pack(pady=20)
        self.calib_next_button.pack_forget()  # Hide this button until calibration starts

        # Tracking Tab
        self.track_button = ttk.Button(self.tracking_tab, text="Start Tracking", command=imp.get_tracker_data)
        self.track_button.pack(pady=20)

        self.duration_entry = ttk.Entry(self.tracking_tab)
        self.duration_entry.pack(pady=20)

        # Log Box
        self.log_box = tk.Text(self.master, height=10)
        self.log_box.pack(padx=10, pady=10, fill=tk.X)
        

    def setup_plot(self):
        self.fig, self.ax = plt.subplots(figsize=(5, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack()
        self.ax.set_xlim(-150, 150)
        self.ax.set_ylim(-150, 150)
        
        self.ax.set_ylabel('Y (cm)')
        self.ax.set_xlabel('X (cm)')
        
        self.ax.set_xticks(range(-150, 151, 100))
        self.ax.set_yticks(range(-150, 151, 100))
        self.ax.set_xticks(range(-150, 151, 50), minor=True)
        self.ax.set_yticks(range(-150, 151, 50), minor=True)
        
        # Enabling grid on the plot - major grid lines
        self.ax.grid(True, which='major', linestyle='-', linewidth=1, color='black')

        # Enabling grid on the plot - minor grid lines, thicker
        self.ax.grid(True, which='minor', linestyle='--', linewidth=0.5, color='blue')

def main():
    root = tk.Tk()
    app = TrackerApplication(root)
    root.mainloop()

if __name__ == '__main__':
    main()
