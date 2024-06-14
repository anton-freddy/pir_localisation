import openvr
import time
import pandas as pd
import matplotlib.pyplot as plt
import ntplib
from datetime import datetime


ntp_client = ntplib.NTPClient()
ntp_server = "pool.ntp.org"


# NTP Time Function
def get_ntp_time(ntp_client, server):
    try:
        response = ntp_client.request(server, version=3)
        ntp_time = datetime.fromtimestamp(response.tx_time)
        return ntp_time.strftime("%H:%M:%S:%f")[:-3]
    except Exception as e:
        print(f"Failed to get NTP time: {e}")
        return datetime.now().strftime("%H:%M:%S:%f")[:-3]


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
    x = pose[0][3] * 100
    y = pose[1][3] * 100
    z = pose[2][3] * 100
    return x, y, z


# Main Function
def main():

    print("Initializing trackers...")
    tracker_indices = initialize_tracker()
    if not tracker_indices:
        print("No trackers found.")
        return

    print(f"Found trackers at indices: {tracker_indices}")
    data = []
    start_time = time.time()

    # Establish home position
    if tracker_indices:
        home_x, home_y, home_z = get_tracker_data(tracker_indices[0])
        print(f"Home position set at X={home_x}, Y={home_y}, Z={home_z}")
        time.sleep(1)

    x_values, z_values = [], []

    try:
        while True:
            current_time = time.time()
            if current_time - start_time > 20:  # Stop after 60 seconds
                break

            for index in tracker_indices:
                x, y, z = get_tracker_data(index)
                relative_x = x - home_x
                relative_z = z - home_z
                x_values.append(relative_x)
                z_values.append(relative_z)
                timestamp = get_ntp_time(ntp_client, ntp_server)
                print(
                    f"Tracker {index}: {timestamp} Relative X={relative_x}, Y={y}, Z={relative_z}"
                )
                data.append(
                    {"Timestamp": timestamp, "X": relative_x, "Y": y, "Z": relative_z}
                )
            time.sleep(0.01)  # Collect data at 10Hz

    except KeyboardInterrupt:
        print("Data collection interrupted.")

    df = pd.DataFrame(data)
    df.to_csv("tracker_data.csv", index=False)
    print("Data saved to tracker_data.csv")

    # Plot the path
    plt.figure(figsize=(10, 10))
    plt.plot(x_values, z_values, marker="o", linestyle="-", color="b")
    plt.title("Top-Down Path View")
    plt.xlabel("X (cm)")
    plt.ylabel("Y (cm)")
    plt.grid(True)
    plt.ylim(-150, 150)
    plt.xlim(-150, 150)
    plt.axis("equal")
    plt.savefig("path_plot.png")
    plt.show()


if __name__ == "__main__":
    main()
