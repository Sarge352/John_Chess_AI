# This is the test file for stockfish
import chess
import chess.engine

# This will create a new chess board
board = chess.Board()

# This will initialize stockfish
engine = chess.engine.SimpleEngine.popen_uci("/path/to/stockfish")

# Get the best move
result = engine.play(board, chess.engine.Limit(time=2.0))
best_move = result.move

# Make the move on the board
board.push(best_move)

