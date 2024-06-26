import openvr
import numpy as np
import time

class HTC_Tracker:
    def __init__(self, offset = [0, 0, 0], log_fnc=None):
        self.log = log_fnc or self.default_log
        self.rotation_matrix = None
        self.translation_vector = None
        
        # Initialize the VR system
        try:
            openvr.init(openvr.VRApplication_Other)
            self.vr_active = 1
        except Exception as e:
            self.log(f'An unexpected error occurred: {type(e).__name__}')
            self.vr_active = 0
            
        try:
            self.vr_system = openvr.VRSystem()
            self.vr_active = 1
        except Exception as e:
            self.log(f'An unexpected error occurred: {type(e).__name__}')        
            self.vr_active = 0
        
        self.offset = offset
        
        
    def default_log(self, message):
        print(message)
    
    def log(self, message):
        self.log(message)
    
    def calibrate(self, global_points, local_points):
        global_points_homogeneous = np.hstack([global_points, np.ones((global_points.shape[0], 1))])
        A, residuals, rank, s = np.linalg.lstsq(global_points_homogeneous, local_points, rcond=None)
        self.rotation_matrix = A[:3, :3]
        self.translation_vector = A[:, 3]
        
    def transform_pose(self, global_pose):
        if self.rotation_matrix is None or self.translation_vector is None:
            self.log("Calibration data not set.")
            return None
        global_pose_homogeneous = np.hstack([global_pose, 1])
        local_pose = self.rotation_matrix.dot(global_pose[:3]) + self.translation_vector
        return local_pose.tolist()

    def get_local_pose(self):
        tracker_index = self.get_device_index(openvr.TrackedDeviceClass_GenericTracker)
        if tracker_index is None:
            self.log("Tracker not found")
            return None

        pose_matrix = self.get_raw_pose(tracker_index)
        if pose_matrix is None:
            self.log("Invalid pose data")
            return None
        
        return self.transform_pose(np.array([pose_matrix[0][3], pose_matrix[1][3], pose_matrix[2][3]]))


    def get_device_index(self, device_class):
        # Find the first device that matches the device class
        for i in range(openvr.k_unMaxTrackedDeviceCount):
            if self.vr_system.getTrackedDeviceClass(i) == device_class:
                return i
        self.log("No Tracker Found!")
        return None

    def get_raw_pose(self, device_index):
        # Get the device poses
        poses = self.vr_system.getDeviceToAbsoluteTrackingPose(openvr.TrackingUniverseStanding, 0, 
                                                               [openvr.TrackedDevicePose_t() for _ in range(openvr.k_unMaxTrackedDeviceCount)])
        pose = poses[device_index]
        if pose.bPoseIsValid:
            return pose.mDeviceToAbsoluteTracking
        else:
            return None

    def get_pose(self, device_index):
        # Get raw pose data
        raw_pose = self.get_raw_pose(device_index)
        if raw_pose is None:
            self.log("Invalid pose data")
            return None

        # Extracting position data (assuming the matrix is a 3x4 matrix)
        position = [raw_pose[0][3], raw_pose[1][3], raw_pose[2][3]]
        # Apply offset to the position
        adjusted_position = [position[i] + self.offset[i] for i in range(3)]
        return adjusted_position

    def set_offset(self, x, y, z):
        # Set the offset values
        self.offset = [x, y, z]
    

    def get_tracker_position(self, raw=False):
        tracker_index = self.get_device_index(openvr.TrackedDeviceClass_GenericTracker)
        if tracker_index is None:
            self.log("Tracker not found")
            return None

        if raw:
            pose_matrix = self.get_raw_pose(tracker_index)
        else:
            return self.get_pose(tracker_index)

        if pose_matrix is None:
            self.log("Invalid pose data")
            return None

        # Extracting position data from the matrix
        return [pose_matrix[0][3], pose_matrix[1][3], pose_matrix[2][3]]

    def close(self):
        openvr.shutdown()