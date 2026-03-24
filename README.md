# Connect 4 AI Bot Skeleton
To get started, download as a zip file. Then, install the requirements:
```
pip install -r requirements.txt
```

To run the game UI, run the command below in the terminal.
```
python main.py
```

You'll be creating your own AI bot to play Connect 4. In order to do that, we first need to agree with the computer what it means to play Connect 4.

# Grids and Boards
Connect 4 is played on a board. A board, or a **grid**, is made from a bunch of squares, or **cells**. You can locate each cell with a **row index** and **column index**.

In our case, we will say that: when you move from top to bottom, row increases.

Similarly: when you move from left to right, column increases.

For example, in a tic-tac-toe board, the top left has row index 0 and column index 0, or (0, 0). The cell all the way below that has position (2, 0).

![tic-tac-toe grid](./assets/row-col-index.png)


To represent a grid in Python, we will use a nested list, or a list inside a list.

Each element in this nested list will represent a row: [row1, row2, row3].

Each row is a list containing the elements of that row: [X, O, O].

This way, we can "visually program" the grid. For example, we can directly draw 3 Xs along the downward diagonal using the nested list below:

[[X, O, O],

 [O, X, O],

 [O, O, X]]

Check if this makes sense by running the command below in the terminal.
```
python checker -q grid_index -u
```

# Cells and Players
Finally, to make the board complete we also need to agree with the computer what is inside each cell.

Here, if a cell is 0, then player 0 has their token inside of there. Same for player 1: if the cell has a 1, then that's player 1's token.

If a cell is -1, then it is empty. The summary is below.

- **-1: empty**
- **0: player 0**
- **1: player 1**

Check if this makes sense by running the command below in the terminal.
```
python checker -q cells -u
```

# Tidy, the Simple AI
The AI makes choices using the `pick_move` function in the `game_ai.py` file. This function takes in the current board and player.

Then, it returns the column as its move. By default, `pick_move` will return `0`, which is the leftmost column. The `pick_move` function can call other functions to create better strategies.

For example, one simple "strategy" is to choose the first open column, starting from the left. We will name this bot "Tidy". Tidy works like this:

1. For each column, check if it is open.
2. If it is open, then return that column index as the move.
3. If it is closed, move on.
4. If Tidy reaches the end without finding an open column, return the last column that was checked.

Test your understanding before writing any code by running:

`python checker -q tidy -u`

After unlocking, write your code in the function named tidy in the game_ai.py file. Then, test your code with:
`python checker -q tidy`

If you want the AI to use this strategy, call the `tidy()` function in the `pick_move()` function.

# Randall, the Random AI
Another strategy is to randomly choose an open column. We will call this strategy "Randall". Randall works like this:

1. First, create a list of all moves.
2. Choose a random move.
3. While this random move is not open, remove it from the list of moves and choose a new random move.
4. Finally, return the move.
5. If there are no moves to make, return the last move selected.

Check your answer by running:

`python checker -q randall`

Hints:
1. To choose a random move from a list, import the `random` library and use the `random.choice()` function. 
```python
import random
options = [5, 6, 7, 8]
choice = random.choice(options)
print(choice) # random element from options
```

2. We provided a function called `is_open()` that checks whether a column is open. It takes in a board and a column. 
```python
board = [[-1, -1, -1],
         [-1, -1, -1],
         [-1, -1, -1]]
print(is_open(board, 0)) # True
```

# Writing your Own Connect 4 Bot
Now it's your turn!

Open up the `game_ai.py` file and fill out the `pick_move` function. This function will take in the current state of the board and the current player, and return the column index of the move that the bot wants to make.

Some helper functions have been provided for you.

# Sources
- [connect-four-ai](https://github.com/benjaminrall/connect-four-ai), for inspiration on computer bot implemented here.
- [perfect connect four ai](https://github.com/lhorrell99/connect-4-solver), for inspiration on how to implement a perfect connect four bot.
- [okpy](https://okpy.github.io/documentation/), for the auto grader.
