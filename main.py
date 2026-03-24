from nicegui import ui
import asyncio
import random
import game_ai

# Constants
EMPTY = -1
PLAYER_0 = 0
PLAYER_1 = 1

def create_board(rows: int=6, columns: int=7) -> list[list[int]]:
    """Create a new Connect 4 board."""
    board = [[EMPTY for j in range(columns)] for i in range(rows)]
    return board

def insert(board: list[list[int]], column: int, player: int) -> bool:
    """Insert a token for the given player into the specified column."""
    rows = len(board)
    for row in range(rows - 1, -1, -1):  # Start from bottom
        if board[row][column] == EMPTY:
            board[row][column] = player

            # player_to_check = 0
            # row_to_check = 5
            # column_to_check = 1
            # if player == player_to_check:
            #     print(game_ai.streak_length(board, player_to_check, row_to_check, column_to_check, 'horizontal'))
            return True
    return False  # Column is full

def check_win(board: list[list[int]], player: int) -> bool:
    """Check if the given player has won the game."""
    rows = len(board)
    cols = len(board[0])

    # Check horizontal
    for row in range(rows):
        for col in range(cols - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Check vertical
    for row in range(rows - 3):
        for col in range(cols):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(rows - 3):
        for col in range(cols - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    # Check diagonal (top-right to bottom-left)
    for row in range(rows - 3):
        for col in range(3, cols):
            if all(board[row + i][col - i] == player for i in range(4)):
                return True

    return False

def is_board_full(board: list[list[int]]) -> bool:
    """Check if the board is completely full (draw condition)."""
    return all(cell != EMPTY for row in board for cell in row)

def get_valid_moves(board: list[list[int]]) -> list[int]:
    """Get a list of valid columns where a piece can be placed."""
    return [col for col in range(len(board[0])) if board[0][col] == EMPTY]

def get_ai_move(board: list[list[int]], player: int) -> int:
    """
    Get a move for the AI player using simple heuristics.

    Args:
        board: Current board state
        player: The AI player (PLAYER_0 or PLAYER_1)

    Returns:
        The column index (0-6) where the AI should place its token
    """
    return game_ai.pick_move(board, player)

def draw_cell(state: int, on_click=None):
    """Draw a single cell on the board."""
    colors = {EMPTY: 'white', PLAYER_0: 'red', PLAYER_1: 'yellow'}
    cell_style = f'background-color: {colors[state]}; border: 2px solid black; border-radius: 50%; width: 50px; height: 50px; margin: 2px;'
    ui.button('', on_click=on_click).style(cell_style).props('flat')

def draw_board(board: list[list[int]], on_cell_click=None):
    """Draw the entire Connect 4 board."""
    with ui.column().style("display: flex; align-items: center;"):
        # Column buttons for dropping pieces
        with ui.row().style("margin-bottom: 10px;"):
            for col in range(len(board[0])):
                ui.button(f'↓', on_click=lambda c=col: on_cell_click(c)).style('width: 50px; height: 30px;')

        # Game board
        with ui.grid(columns=len(board[0])).style("border: 3px solid black; padding: 10px; background-color: blue;"):
            for row in range(len(board)):
                for col in range(len(board[0])):
                    draw_cell(board[row][col])

class ConnectFourGame:
    def __init__(self):
        self.board = create_board()
        self.current_player = PLAYER_0
        self.game_over = False
        self.winner = None
        self.game_mode = "human_vs_human"  # "human_vs_human" or "human_vs_computer"
        self.board_ui = None
        self.status_label = None
        self.reset_button = None
        self.mode_selector = None

    def set_game_mode(self, mode: str):
        """Set the game mode and reset the game."""
        self.game_mode = mode
        self.reset_game()

    def reset_game(self):
        """Reset the game to initial state."""
        self.board = create_board()
        self.current_player = PLAYER_0
        self.game_over = False
        self.winner = None
        self.update_ui()

        # If computer goes first in human vs computer mode
        if self.game_mode == "human_vs_computer" and self.current_player == PLAYER_1:
            asyncio.create_task(self.make_computer_move())

    def is_human_turn(self) -> bool:
        """Check if it's currently a human player's turn."""
        if self.game_mode == "human_vs_human":
            return True
        elif self.game_mode == "human_vs_computer":
            return self.current_player == PLAYER_0  # Human is always PLAYER_0
        return True

    async def make_computer_move(self):
        """Make a move for the computer player."""
        if self.game_over or self.is_human_turn():
            return

        # Add a small delay to make the computer move feel more natural
        await asyncio.sleep(0.5)

        # Get AI move
        column = get_ai_move(self.board, self.current_player)

        # Make the move
        self.make_move(column, is_computer_move=True)

    def make_move(self, column: int, is_computer_move: bool = False):
        """Handle a player's move in the specified column."""
        # Prevent human moves when it's not their turn
        if not is_computer_move and self.game_mode == "human_vs_computer" and not self.is_human_turn():
            return
        
        # Prevent computer moves when it's not their turn
        if is_computer_move and self.game_mode == "human_vs_computer" and self.is_human_turn():
            return

        if insert(self.board, column, self.current_player):
            if check_win(self.board, self.current_player):
                self.game_over = True
                self.winner = self.current_player
            elif is_board_full(self.board):
                self.game_over = True
                self.winner = None  # Draw
            else:
                self.current_player = PLAYER_1 if self.current_player == PLAYER_0 else PLAYER_0

                # If it's now the computer's turn, make the computer move
                if not self.is_human_turn() and not self.game_over:
                    asyncio.create_task(self.make_computer_move())

        
        
        self.update_ui()

    def update_ui(self):
        """Update the UI to reflect the current game state."""
        # Clear the board container and redraw
        if self.board_ui:
            self.board_ui.clear()
            with self.board_ui:
                draw_board(self.board, self.make_move)

        # Update status
        if self.status_label:
            if self.game_over:
                if self.winner is not None:
                    player_name = "Red" if self.winner == PLAYER_0 else "Yellow"
                    if self.game_mode == "human_vs_computer":
                        if self.winner == PLAYER_0:
                            self.status_label.text = f"🎉 You win!"
                        else:
                            self.status_label.text = f"🤖 Computer wins!"
                    else:
                        self.status_label.text = f"🎉 {player_name} wins!"
                else:
                    self.status_label.text = "🤝 It's a draw!"
            else:
                if self.game_mode == "human_vs_computer":
                    if self.is_human_turn():
                        self.status_label.text = "Your turn (Red)"
                    else:
                        self.status_label.text = "🤖 Computer is thinking..."
                else:
                    player_name = "Red" if self.current_player == PLAYER_0 else "Yellow"
                    emoji = "🔴" if self.current_player == PLAYER_0 else "🟡"
                    self.status_label.text = f"{player_name}'s turn {emoji}"

        # Show/hide reset button
        if self.reset_button:
            self.reset_button.visible = self.game_over

# Create the game instance
game = ConnectFourGame()

# Create the UI
with ui.card().style('max-width: 600px; margin: auto;'):
    ui.label('Connect Four').style('font-size: 24px; font-weight: bold; text-align: center; margin-bottom: 20px;')

    # Game mode selector
    with ui.row().style('justify-content: center; margin-bottom: 15px;'):
        ui.label('Game Mode:').style('margin-right: 10px;')
        game.mode_selector = ui.select(
            options={
                'human_vs_human': 'Human vs Human',
                'human_vs_computer': 'Human vs Computer'
            },
            value='human_vs_human',
            on_change=lambda e: game.set_game_mode(e.value)
        ).style('width: 200px;')

    # Status label
    game.status_label = ui.label("Red's turn").style('font-size: 18px; text-align: center; margin-bottom: 10px;')

    # Board container
    game.board_ui = ui.column()

    # Reset button (initially hidden)
    game.reset_button = ui.button('New Game', on_click=game.reset_game).style('margin-top: 20px;')
    game.reset_button.visible = False

# Initialize the board
game.update_ui()

# Run the app only when executed directly
if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='Connect Four', favicon='./assets/randall.png', port=8000)
