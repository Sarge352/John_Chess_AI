# This is a test file for openCV
import cv2

# Start video capture
cap = cv2.VideoCapture(0) # 0 is the default value for the camera index. If we are using multiple cameras, we can change the value 
                          # for each camera. Cap is used to the frames on the camera.

# Check to make sure the camera is open or not
if cap.isOpened():
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
else:
  print("Camera is not connected.")

#Releases the capture after everything else is done
cap.release()
cv2.destroyAllWindows()
