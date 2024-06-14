import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import ntplib
from datetime import datetime
import json
import os
import pandas as pd
import openvr
import time

ntp_client = ntplib.NTPClient()
        # Initialize NTP
ntp_server = 'pool.ntp.org'

class TrackerApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Tracker System Control")



        #openvr.init(openvr.VRApplication_Background)
        # Configuration data
        self.config_path = 'config.json'
        self.load_config()
        
        # Define calibration positions
        self.calibration_positions = [
            (100, -100), (100, 0), (100, 100),
            (0, -100), (0, 0), (0, 100),
            (-100, -100), (-100, 0), (-100, 100)
        ]
        self.calibration_index = 0
        self.calibration_measurements = []
        self.calibration_offset = []

        self.tracker_i = self.initialize_tracker()
        
        # GUI Setup
        self.setup_gui()
        self.setup_plot()

    def load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {'calibration_data': {}}

    def save_config(self):
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f)

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
        self.track_button = ttk.Button(self.tracking_tab, text="Start Tracking", command=self.start_tracking)
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

    def log_message(self, message):
        self.log_box.insert(tk.END, message + "\n")
        self.log_box.see(tk.END)

    def start_calibration(self):
        self.calibration_index = 0
        self.calibration_measurements = []
        self.calib_button.pack_forget()
        self.calib_next_button.pack(pady=20)
        self.prompt_calibration_step()
        
    def prompt_calibration_step(self):
        if self.calibration_index < len(self.calibration_positions):
            pos = self.calibration_positions[self.calibration_index]
            self.calibration_label.config(text=f"Place the tracker at position {self.calibration_index + 1}: {pos}")
        else:
            self.finish_calibration()
            
    def record_position(self):
        if self.calibration_index < len(self.calibration_positions):
            # Fetch tracker data at the current position
            
            for index in self.tracker_i:
                    x, y, z = self.get_tracker_data(index)
                    measured_x = x
                    measured_z = z

            self.log_message(f"X: {measured_x} Z: {measured_z}")
            # Get the predefined calibration position
            target_x, target_z = self.calibration_positions[self.calibration_index]
            # Calculate offsets
            offset_x = measured_x - target_x
            offset_z = measured_z - target_z
            
            self.log_message(f"X Offset: {offset_x} Z Offset: {offset_z}")
            # Store the offsets
            self.calibration_measurements.append((offset_x, offset_z))
            self.calibration_index += 1
            self.prompt_calibration_step()
        else:
            self.finish_calibration()
                
    def finish_calibration(self):
        if self.calibration_measurements:
            # Calculate the average of the offsets
            avg_offset_x = sum(pos[0] for pos in self.calibration_measurements) / len(self.calibration_measurements)
            avg_offset_z = sum(pos[1] for pos in self.calibration_measurements) / len(self.calibration_measurements)
            # Store the average offsets in the configuration
            self.config['calibration_offsets'] = {'offset_x': avg_offset_x, 'offset_z': avg_offset_z}
            self.save_config()
            self.log_message(f"Calibration complete. Average offsets: X={avg_offset_x}, Z={avg_offset_z}")
            messagebox.showinfo("Calibration Complete", "Calibration is successfully completed!")
            self.tab_control.select(self.tracking_tab)  # Switch to tracking tab
        else:
            self.log_message("Calibration failed: No data recorded.")
            messagebox.showerror("Calibration Error", "Calibration failed due to insufficient data.")

    def initialize_tracker(self):
        poses = []
      #  for device in range(openvr.k_unMaxTrackedDeviceCount):
      #      if openvr.VRSystem().getTrackedDeviceClass(device) == openvr.TrackedDeviceClass_GenericTracker:
      #          poses.append(device)
        return poses

    def start_tracking(self):
        duration = int(self.duration_entry.get())
        self.log_message("Initializing trackers...")
        tracker_indices = self.tracker_i
        tracker_indices = self.initialize_tracker()
        if not tracker_indices:
           self.log_message("No trackers found.")
           return

        self.log_message(f"Found trackers at indices: {tracker_indices}")
        threading.Thread(target=self.track, args=(tracker_indices,duration)).start()

    def track(self, tracker_indices, duration):
        data = []
        offset_x = self.config['calibration_offsets']['offset_x']
        offset_z = self.config['calibration_offsets']['offset_z']
        start_time = datetime.now()
        try:
            while (datetime.now() - start_time).seconds < duration:  
                for index in tracker_indices:
                    x, y, z = self.get_tracker_data(index)
                    relative_x = x - offset_x
                    relative_z = z - offset_z
                    timestamp = self.get_ntp_time()
                    self.log_message(f"Tracker {index}: {timestamp} Relative X={relative_x}, Z={relative_z}")
                    data.append({"Timestamp": timestamp, "X": relative_x, "Z": relative_z})
                    time.sleep(0.01)
                    
                self.update_plot(relative_x, relative_z)  # Update the plot in real-time
        except Exception as e:
            self.log_message(f"Error during tracking: {e}")

        df = pd.DataFrame(data)
        df.to_csv("tracker_data.csv", index=False)
        self.log_message("Data saved to tracker_data.csv")
        self.canvas.print_png("image.png")
        
    def get_tracker_data(self, tracker_index):
        pose = openvr.VRSystem().getDeviceToAbsoluteTrackingPose(openvr.TrackingUniverseStanding, 0, openvr.k_unMaxTrackedDeviceCount)[tracker_index].mDeviceToAbsoluteTracking
        x = pose[0][3] * 100
        y = pose[1][3] * 100
        z = pose[2][3] * 100
        return x, y, z

    def update_plot(self, x, z):
        self.ax.scatter(x, z, color='red')
        self.canvas.draw()

    def get_ntp_time(self):
        try:
            response = ntp_client.request(ntp_server, version=3)
            return datetime.fromtimestamp(response.tx_time).strftime("%H:%M:%S:%f")[:-3]
        except Exception as e:
            self.log_message(f"Failed to get NTP time: {e}")
            return datetime.now().strftime("%H:%M:%S:%f")[:-3]

def main():
    root = tk.Tk()
    app = TrackerApplication(root)
    root.mainloop()

if __name__ == '__main__':
    main()
