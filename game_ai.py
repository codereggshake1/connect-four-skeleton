import random

##############################
# Tidy, the Simple AI
def tidy(board: list[list[int]], player: int) -> int:
    """
    TODO: Fill out Tidy's strategy
    1. For each column, check if it is open.
    2. If it is open, then return that column as the move.
    3. If it is closed, move on.
    If Tidy reached the end without finding an open column, return the last column that was checked.
    """
    for move in range(len(board[0])):
        if is_open(board, move):
            return move
    return move

##############################
# Randall, the Random AI
def randall(board: list[list[int]], player: int) -> int:
    """
    TODO: Fill out Randall's strategy
    1.First, create a list of all moves.
    2. Choose a random move.
    3. While this random move is not open, remove it from the list of moves and choose a new random move.
    4. Finally, return the move.
    If there are no moves to make, return the last move selected.
    """
    num_cols = len(board[0])
    moves = list(range(num_cols))
    move = random.choice(moves)
    # print(f"choice {move} from {moves}")
    while not is_open(board, move) and len(moves) > 0:
        moves.remove(move)
        move = random.choice(moves)
        # print(f"choice {move} from {moves}")
    return move

##############################
# TODO: Write a connect four game AI!
# When you're ready, run `python main.py` to test your AI in the game.
def pick_move(board: list[list[int]], player: int) -> int:
    """
    TODO: Pick a better move than the left most column
    Pick the best move for the AI player based on the current board state.
    
    Args:
        board: The current game board as a 2D list.
        player: The AI player's number (0 or 1).
        Returns: The column index (0-6) where the AI should place its token.
    """
    # Choose a better move than the left most column
    return 0

##############################
# Helper functions for AI logic (optional, but can be useful for more advanced strategies)
def get_column(board: list[list[int]], col: int) -> list[int]:
    """
    Get the entire column as a list, with the top row as the beginning of the list.
    
    Args:
        board: The current game board as a 2D list.
        col: The column index to check (0-6).
    Returns: A list of all values in the specified column.
    """
    return [board[row][col] for row in range(6)]

def get_row(board: list[list[int]], row: int) -> list[int]:
    """
    Get the entire row.
    
    Args:
        board: The current game board as a 2D list.
        row: The row index to check (0-5).
    Returns: A list of all values in the specified row.
    """
    return board[row]

def get_adjacent(board: list[list[int]], row: int, col: int, direction='left') -> int|None:
    """
    Get the adjacent cell value in the specified direction.
    
    Args:
        board: The current game board as a 2D list.
        row: The row index of the current cell (0-5).
        col: The column index of the current cell (0-6).
        direction: The direction to check ('left', 'right', 'up', 'down').
    Returns: The value of the adjacent cell in the specified direction, or None if out of bounds.
    """
    if direction == 'left' and col > 0:
        return board[row][col - 1]
    elif direction == 'right' and col < 6:
        return board[row][col + 1]
    elif direction == 'up' and row > 0:
        return board[row - 1][col]
    elif direction == 'down' and row < 5:
        return board[row + 1][col]
    return None

def is_open(board: list[list[int]], col: int) -> bool:
    """
    Check if a move is valid (i.e., the column is not full).
    
    Args:
        board: The current game board as a 2D list.
        col: The column index to check (0-6).
    Returns: True if the move is valid, False otherwise.
    """
    return board[0][col] == -1  # Check if the top cell of the column is empty

def three_in_a_row(board: list[list[int]], player: int) -> bool:
    """
    Check if the given player has three in a row (potential winning move).
    
    Args:
        board: The current game board as a 2D list.
        player: The player's number (0 or 1).
    Returns: True if the player has three in a row, False otherwise.
    """    
    # Check horizontal, vertical, and diagonal for three in a row
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (col <= 3 and all(board[row][col + i] == player for i in range(3))) or \
               (row <= 2 and all(board[row + i][col] == player for i in range(3))) or \
               (col <= 3 and row <= 2 and all(board[row + i][col + i] == player for i in range(3))) or \
               (col >= 3 and row <= 2 and all(board[row + i][col - i] == player for i in range(3))):
                return True
    return False

def streak_length(board: list[list[int]], player: int, row: int, col: int, direction: str) -> int:
    """
    Calculate the length of the streak for the given player in the specified direction.
    For example, if there's a three-in-a-row horizontally, this function would return 3 for any of those three pieces, including the middle piece.
    
    Args:
        board: The current game board as a 2D list.
        player: The player's number (0 or 1).
        row: The starting row index (0-5).
        col: The starting column index (0-6).
        direction: The direction to check ('horizontal', 'vertical', 'diagonal_up', 'diagonal_down').
    Returns: The length of the streak in the specified direction.
    """
    max_left = 0
    max_right = 0 # can return max_right - max_left + 1
    if board[row][col] != player:
        return 0  # No streak if the starting cell doesn't belong to the player
    
    if direction == 'horizontal':
        # check left
        for c in range(col - 1, -1, -1):
            if board[row][c] == player:
                max_left -= 1
            else:
                break
        # check right
        for c in range(col + 1, 7):
            if board[row][c] == player:
                max_right += 1
            else:
                break
    elif direction == 'vertical':
        # check up
        for r in range(row - 1, -1, -1):
            if board[r][col] == player:
                max_left -= 1
            else:
                break
        # check down
        for r in range(row + 1, 6):
            if board[r][col] == player:
                max_right += 1
            else:
                break
    elif direction == 'diagonal_up':
        # check up-left
        for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[r][c] == player:
                max_left -= 1
            else:
                break
        # check down-right
        for r, c in zip(range(row + 1, 6), range(col + 1, 7)):
            if board[r][c] == player:
                max_right += 1
            else:
                break
    elif direction == 'diagonal_down':
        # check down-left
        for r, c in zip(range(row + 1, 6), range(col - 1, -1, -1)):
            if board[r][c] == player:
                max_left -= 1
            else:
                break
        # check up-right
        for r, c in zip(range(row - 1, -1, -1), range(col + 1, 7)):
            if board[r][c] == player:
                max_right += 1
            else:
                break
    return max_right - max_left + 1
