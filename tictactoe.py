"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Initiate a turn counter variable
    turnsLeft = 0

    # Count how many turns are left
    for row in board:
        for cell in row:
            if cell == EMPTY:
                turnsLeft += 1

    # If number of turns is even, X must've turned
    if turnsLeft % 2 == 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Initialize an empty set
    emptyCells = set()
    
    # Check for empty cells
    for row in range(len(board)):
        for cell in range(len(board[0])): 
            if board[row][cell] == EMPTY:
                emptyCells.add((row, cell))

    # Return a set of empty cells
    return emptyCells


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Create a copy of the board
    boardCopy = deepcopy(board)
    boardCopy[action[0]][action[1]] = player(board)
    return boardCopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Checks for a win (horizontally or vertically)
    for line in range(3):
        if board[line][0] == board[line][1] == board[line][2] != EMPTY:
            return board[line][0]
        elif board[0][line] == board[1][line] == board[2][line] != EMPTY:
            return board[0][line]   
        
    # Checks for a win (diagonally)
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    # Tie
    return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Checks if there is a winner, then ends the game
    if winner(board) is not None:
        return True
    
    # Checks if the board is full and no winner, then ends the game
    full_board = True
    for row in board:
        if EMPTY in row:
            full_board = False
            break

    if full_board and winner(board) is None:
        return True
    
    # Game has not ended yet
    return False
        

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Checks if winner is O or X
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Checks if the game has ended and what the AI is playing
    if terminal(board):
        return None
    else:
        if player(board) == X:
            return max_value(board)[1]
        elif player(board) == O:
            return min_value(board)[1]
 
def max_value(board):
    """
    Returns maximum value
    """
    if terminal(board):
        return utility(board), None
    
    # Initialize positive infinity and optimal solution
    v = float(-math.inf)
    optimalSolution = None

    # Find the optimal solution while considering the opponent's moves  
    for action in actions(board):
        highest, _ = min_value(result(board, action))
        if highest > v:
            v = highest
            optimalSolution = action
            if v == 1:
                return v, optimalSolution
            
    return v, optimalSolution
 
def min_value(board):
    """
    Returns minimum value
    """
    if terminal(board):
        return utility(board), None
    
    # Initialize negative infinity and optimal solution
    v = float(math.inf)
    optimalSolution = None

    # Find the optimal solution while considering the opponent's moves
    for action in actions(board):
        lowest, _ = max_value(result(board, action))
        if lowest < v:
            v = lowest
            optimalSolution = action
            if v == -1:
                return v, optimalSolution
            
    return v, optimalSolution

