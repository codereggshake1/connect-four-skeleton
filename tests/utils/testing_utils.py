def is_open(board: list[list[int]], col: int) -> bool:
    """
    Check if a move is valid (i.e., the column is not full).
    
    Args:
        board: The current game board as a 2D list.
        col: The column index to check (0-6).
    Returns: True if the move is valid, False otherwise.
    """
    return board[0][col] == -1  # Check if the top cell of the column is empty


def proportions(board, player, strategy, n=100):
    num_columns = len(board[0])
    props = [0 for _ in range(num_columns)]
    for i in range(n):
            props[strategy(board, player)] += 1
    props = list( map(lambda c: c/n, props) )
    # only take proportions that have an open column
    open_props = [props[i] for i in range(num_columns) if is_open(board, i)]
    return open_props

def is_uniform(props):
    return all( list(map(lambda p: abs(p - 1/len(props)) <= .1, props)) )
