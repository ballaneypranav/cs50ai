"""
Tic Tac Toe Player
"""

import math
import copy

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
    numX, numO = 0, 0
    for row in board:
        for cell in row:
            if cell == X:
                numX += 1
            elif cell == O:
                numO += 1
    
    if numX > numO:
        return O
    elif not terminal(board) and numX == numO:
        return X
    else:
        return None

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                result.add((i, j))
    return result

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if terminal(board):
        raise GameOver
    elif action not in actions(board):
        raise InvalidAction
    else:
        p = player(board)
        result_board = copy.deepcopy(board)
        (i, j) = action
        result_board[i, j] = p

    return result_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    if not terminal(board):
        return None

    if board[0,0] == board[0,1] == board[0,2]:
        if board[0,0] == X:
            return X
        else:
            return O
    elif board[1,0] == board[1,1] == board[1,2]: 
        if board[1,0] == X:
            return X
        else:
            return O
    elif board[2,0] == board[2,1] == board[2,2]:
        if board[2,0] == X:
            return X
        else:
            return O
    elif board[0,0] == board[1,0] == board[2,0]:
        if board[0,0] == X:
            return X
        else:
            return O
    elif board[0,1] == board[1,1] == board[2,1]:
        if board[0,1] == X:
            return X
        else:
            return O
    elif board[0,2] == board[1,2] == board[2,2]:
        if board[0,2] == X:
            return X
        else:
            return O
    elif board[0,0] == board[1,1] == board[2,2]:
        if board[0,0] == X:
            return X
        else:
            return O
    elif board[0,2] == board[1,1] == board[2,0]:
        if board[0,2] == X:
            return X
        else:
            return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class GameOver(Error):
    """Game over.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = "Terminal board."
        self.message = "Game over."

class InvalidAction(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = "Invalid action."
        self.message = "Invalid action." 