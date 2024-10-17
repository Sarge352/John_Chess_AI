# This is a test file for openCV
import cv2


print(cv2.__version__)
# Start video capture
cap = cv2.VideoCapture(0)  # 0 is the default value for the camera index. 
                           # If using multiple cameras, change the value for each camera.
                           # 'cap' captures frames from the camera.

# Function to highlight the AI's move using OpenCV
def highlight_move(ai_best_move, cap):

    while True:
        ret, frame = cap.read()  # Reads the frame from the camera. 
        if not ret:
            break # Breaks the loop if there is an issue with capturing. 

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
        cv2.imshow("Chess Board", frame)  # Allows us to see what the camera/ai sees.

        # Process the frame (e.g., detect pieces)
        # For example: cv2.imshow("Chess Board", frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()