import openvr
import time
import csv

# Initialize OpenVR
openvr.init(openvr.VRApplication_Other)

# Set up CSV file for data recording
with open('tracker_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Time', 'X', 'Y', 'Z'])  # Column headers

    start_time = time.time()
    while (time.time() - start_time) < 30:  # Record for 30 seconds
        # Get pose data for the tracker
        poses = openvr.VRSystem().getDeviceToAbsoluteTrackingPose(
            openvr.TrackingUniverseStanding, 0, openvr.k_unMaxTrackedDeviceCount)
        
        # Find the tracker and record its position
        for i in range(openvr.k_unMaxTrackedDeviceCount):
            pose = poses[i]
            if pose.bDeviceIsConnected and pose.bPoseIsValid:
                device_class = openvr.VRSystem().getTrackedDeviceClass(i)
                if device_class == openvr.TrackedDeviceClass_GenericTracker:
                    # Access the position matrix directly
                    matrix = pose.mDeviceToAbsoluteTracking
                    position = (matrix[0][3], matrix[1][3], matrix[2][3])
                    writer.writerow([time.time(), position[0], position[1], position[2]])
                    break  # Assume one tracker for simplicity

        time.sleep(0.1)  # Delay to prevent too high polling rate

# Clean up OpenVR
openvr.shutdown()
