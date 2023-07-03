# Tic-Tac-Toe AI

This is an implementation of an AI player for the game Tic-Tac-Toe. The AI is designed to play the game intelligently by using the minimax algorithm to search for the optimal move.

## How to Run

To run the Tic-Tac-Toe AI, you will need to have Python installed on your system. Clone this repository and navigate to the project directory. Then, run the following command:

```
python runner.py
```

1. Choose to play as either "X" or "O".
2. Click on an empty cell to make a move.
3. The game ends when there is a winner or a tie.
4. Click on "Play Again" to start a new game.

## Files

- `runner.py`: The main file that runs the Tic-Tac-Toe game and AI player. It uses the Pygame library for the graphical user interface.

- `tictactoe.py`: Contains the game logic and functions for managing the Tic-Tac-Toe board, including player turns, actions, and the minimax algorithm.

## Dependencies

The Tic-Tac-Toe AI requires the Pygame library to be installed. You can install it using pip:

```
pip install pygame
```

## How the AI Works

The Tic-Tac-Toe AI uses the minimax algorithm to determine the optimal move for the current player. The minimax algorithm is a recursive algorithm that evaluates all possible moves and chooses the move that leads to the best outcome.

The AI follows the following steps to play the game:

1. Determine the player who has the next turn.
2. If it is the AI's turn, apply the minimax algorithm to find the best move.
3. If it is the user's turn, wait for a click event to make a move.
4. Check if the game has ended after each move.
5. If the game has ended, display the result and provide an option to play again.
