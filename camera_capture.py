# camera_capture.py

import cv2
import time

def start_camera():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None  # Return None if the camera couldn't be opened

    time.sleep(2)  # Wait for camera to initialize
    return cap  # Return the VideoCapture object