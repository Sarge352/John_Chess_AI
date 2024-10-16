# This is a test file for openCV
import cv2

# Start video capture
cap = cv2.VideoCapture(0)  # 0 is the default value for the camera index. 
                           # If using multiple cameras, change the value for each camera.
                           # 'cap' captures frames from the camera.

# Function to highlight the AI's move using OpenCV
def highlight_move(ai_best_move, cap):

    while True:
        ret, frame = cap.read()  # Capture frame
        if not ret:
            break

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Thresholding
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw contours
        for contour in contours:
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

        # Highlight the AI's move if it exists
        if ai_best_move:
            start_square = ai_best_move[:2]  # e.g., 'e2'
            end_square = ai_best_move[2:]    # e.g., 'e4'

            # Map the chessboard square to coordinates
            start_position = map_square_to_coordinates(start_square)
            end_position = map_square_to_coordinates(end_square)

            # Draw a circle around the piece to move
            cv2.circle(frame, start_position, radius=10, color=(0, 0, 255), thickness=2)

            # Draw an arrow to the destination square
            cv2.arrowedLine(frame, start_position, end_position, color=(255, 0, 0), thickness=2)

        # Show the processed frame
        cv2.imshow("Chess Board", frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to map UCI chess notation (e.g., 'e2') to pixel coordinates
def map_square_to_coordinates(square):
    # Implement this to map chess notation to actual chessboard coordinates
    square_to_index = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7
    }

    # Extract the column (file) and row (rank) from the chess notation
    column = square[0]  # 'e' in 'e2'
    row = int(square[1])  # '2' in 'e2'

    # Calculate the pixel coordinates
    # Adjust 80 pixels per square (assuming 640x640 resolution for an 8x8 board)
    x = square_to_index[column] * 80 + 40  # Center of the square horizontally
    y = (8 - row) * 80 + 40  # Center of the square vertically, flip since top row is '8'

    return (x, y)