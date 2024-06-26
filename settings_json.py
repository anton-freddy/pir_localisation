import json
import os

# Contents
JSON_x_min_max = 'x_limits'
JSON_y_min_max = 'y_limits'
JSON_calibration_array = 'calibration_positions'

class JSONSettingsHandler:
    def __init__(self, filepath, log_fnc=None):
        self.log = log_fnc or self.default_log
        self.filepath = filepath
        self.settings = self.load_settings()
        
        
    def default_log(self, message):
        print(message)
    
    def log(self, message):
        self.log(message)

    def load_settings(self):
        try:
            if os.path.exists(self.filepath) and os.path.getsize(self.filepath) > 0:
                with open(self.filepath, 'r') as file:
                    return json.load(file)
            else:
                return {}
        except json.JSONDecodeError:
            self.log(f"Error decoding JSON from {self.filepath}. Starting with empty settings.")
            return {}
        except Exception as e:
            self.log(f"Unexpected error loading settings: {e}")
            return {}

    def save_settings(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def get_setting(self, key):
        return self.settings.get(key, None)

    def set_setting(self, key, value):
        self.settings[key] = value
        self.save_settings()
