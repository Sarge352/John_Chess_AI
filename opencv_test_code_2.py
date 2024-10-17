# This is a test file for OpenCV
import cv2
from camera_capture import start_camera  # Import the function from the camera module

print(cv2.__version__)

# Start video capture
cap = start_camera()  # Call the function to start the camera

if cap is None:
    print("Camera could not be opened.")
    exit()  # Exit if the camera couldn't be opened

# Function to highlight the AI's move using OpenCV
def highlight_move(ai_best_move, cap):
    while True:
        ret, frame = cap.read()  # Reads the frame from the camera.
        if not ret:
            print("Error: Could not read frame.")
            break  # Breaks the loop if there is an issue with capturing.

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Thresholding
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        # Finding contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw contours
        for contour in contours:
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)  # Draw contours in green

        # Show the processed frame
        cv2.imshow("Chess Board", frame)  # Allows us to see what the camera/AI sees.

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Call the highlight function (for testing)
highlight_move(None, cap)

cap.release()
cv2.destroyAllWindows()