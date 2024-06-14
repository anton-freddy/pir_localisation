import openvr
import time
import pandas as pd
import matplotlib.pyplot as plt
import ntplib
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog
import tkinter.scrolledtext as ScrolledText
import json


# Initialize NTP client globally
ntp_client = ntplib.NTPClient()
ntp_server = 'pool.ntp.org'

def get_ntp_time(server):
    global ntp_client  # Declare the use of the global variable
    try:
        response = ntp_client.request(server, version=3)
        ntp_time = datetime.fromtimestamp(response.tx_time)
        return ntp_time.strftime("%H:%M:%S:%f")[:-3]
    except Exception as e:
        log_message(f"Failed to get NTP time: {e}")
        return datetime.now().strftime("%H:%M:%S:%f")[:-3]

# Ensure other functions that use ntp_client declare it as global if needed



# Initialization and Tracking Functions
def initialize_tracker():
    openvr.init(openvr.VRApplication_Background)
    poses = []
    for device in range(openvr.k_unMaxTrackedDeviceCount):
        device_class = openvr.VRSystem().getTrackedDeviceClass(device)
        if device_class == openvr.TrackedDeviceClass_GenericTracker:
            poses.append(device)
    return poses


def get_tracker_data(tracker_index):
    pose = (
        openvr.VRSystem()
        .getDeviceToAbsoluteTrackingPose(
            openvr.TrackingUniverseStanding, 0, openvr.k_unMaxTrackedDeviceCount
        )[tracker_index]
        .mDeviceToAbsoluteTracking
    )
    x = pose[0][3] * 1000
    y = pose[1][3] * 1000
    z = pose[2][3] * 1000
    return x, y, z


def save_home_position(home_position):
    with open("home_position.json", "w") as f:
        json.dump(home_position, f)


def load_home_position():
    try:
        with open("home_position.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None


# GUI Functions
def set_home():
    global home_x, home_y, home_z
    home_x, home_y, home_z = get_tracker_data(0)  # Assume tracker at index 0
    time.sleep(5)
    save_home_position({"home_x": home_x, "home_y": home_y, "home_z": home_z})
    log_message(f"Home position set at X={home_x}, Y={home_y}, Z={home_z}")


def start_tracking():
    duration = simpledialog.askinteger(
        "Input", "Enter the tracking duration in seconds:"
    )
    if duration is None:
        return

    start_time = time.time()
    data = []
    x_values = []  # Corrected list initialization
    z_values = []  # Corrected list initialization
    while True:
        current_time = time.time()
        if current_time - start_time > duration:
            break
        x, y, z = get_tracker_data(0)  # Assuming index 0, adjust if necessary
        relative_x = x - home_x
        relative_z = z - home_z
        x_values.append(relative_x)
        z_values.append(relative_z)
        timestamp = get_ntp_time(ntp_server)
        log_message(f"Relative X={relative_x}, Y={y}, Z={relative_z}, Time={timestamp}")
        data.append({"Timestamp": timestamp, "X": relative_x, "Y": y, "Z": relative_z})
        time.sleep(0.1)

    df = pd.DataFrame(data)
    df.to_csv("tracker_data.csv", index=False)
    log_message("Data saved to tracker_data.csv")

    plt.figure(figsize=(10, 10))
    plt.plot(x_values, z_values, marker="o", linestyle="-", color="b")
    plt.title("Top-Down Path View")
    plt.xlabel("X (mm)")
    plt.ylabel("Z (mm)")
    plt.grid(True)
    plt.axis("equal")
    plt.savefig("path_plot.png")
    plt.show()


def log_message(message):
    log_box.insert(tk.END, message + "\n")
    log_box.see(tk.END)  # Auto-scroll to the bottom

# Main GUI
root = tk.Tk()
root.title("Tracker Control Panel")
initialize_tracker()

# ScrolledText widget for logging
log_box = ScrolledText.ScrolledText(root, height=10, width=70)
log_box.pack(padx=10, pady=10)


home_button = tk.Button(root, text="Set Home Position", command=set_home)
home_button.pack(pady=20)

track_button = tk.Button(root, text="Start Tracking", command=start_tracking)
track_button.pack(pady=20)

root.mainloop()
