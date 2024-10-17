# This is the test file for stockfish
import chess
from stockfish import Stockfish
from opencv_test_code_2 import *

# This will create a new chess board
board = chess.Board()

# Initialize the Stockfish engine using the stockfish package
stockfish = Stockfish("C:\\Users\\user\\OneDrive\\Desktop\\stockfish\\stockfish\\stockfish-windows-x86-64-avx2.exe")

# Function to get the best move from Stockfish
def get_best_move(fen_string):
    stockfish.set_fen_position(fen_string)
    return stockfish.get_best_move()

# Function to handle the AI's move
def ai_move(board):
    try:
        # Get the FEN string from the current board position
        board_fen = board.fen()

        # Use Stockfish to get the best move
        best_move_str = get_best_move(board_fen)
        print(f"AI's best move: {best_move_str}")

        # Convert Stockfish's move string to a chess.Move object
        best_move = chess.Move.from_uci(best_move_str)

        # Ensure the move is legal
        if board.is_legal(best_move):
            # Make the move on the board
            board.push(best_move)
            return best_move
        else:
            print("Stockfish suggested an illegal move.")
    except Exception as e:
        print(f"Error occurred while making AI move: {e}")
        return None

# Function to handle the user's move
def user_move(board):
    while True:
        try:
            # Ask the user for their move
            user_move_str = input("Enter your move in UCI format (e.g., e2e4): ")

            # Convert the input to a chess.Move object
            user_move = chess.Move.from_uci(user_move_str)

            # Validate the move
            if board.is_legal(user_move):
                # Push the move onto the board
                board.push(user_move)
                return user_move
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input format. Please enter a move in UCI format.")
        except Exception as e:
            print(f"Error occurred while processing user move: {e}")

# Main game loop: User vs AI
def play_game():
    stockfish.set_skill_level(10)  # Set the AI's difficulty level to 10 (can be changed)
                                   # Skill level ranges from 0 (weakest) to 20 (strongest)

    while not board.is_game_over():
        print(board)  # Print the current board position

        # Check if it's check, checkmate, or stalemate
        if board.is_checkmate():
            print("Checkmate! Game over.")
            break
        elif board.is_stalemate():
            print("Stalemate! It's a draw.")
            break
        elif board.is_check():
            print("Check!")

        # User's turn
        print("Your move:")
        user_move(board)

        # Check game state after user's move
        if board.is_game_over():
            break

        # AI's turn
        print("AI's move:")
        ai_best_move = ai_move(board)

        # Check game state after AI's move
        if board.is_game_over():
            break

        # Highlight AI's move using OpenCV
        highlight_move(ai_best_move, cap)  # Call the OpenCV function and pass the move

    print("Final board position:")
    print(board)
    print("Game over.")

# Run the game
play_game()


#test


