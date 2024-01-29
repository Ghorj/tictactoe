"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state() -> list:
    """
    Returns starting state of the board.

    Returns:
        empty board (list)
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board) -> str:
    """
    Returns player who has the next turn on a board.

    Input:
        board (list)
    Returns:
        player (str)
    """
    # initialise counters
    x_count = 0
    o_count = 0

    # count the number of pieces on the board
    for row in board:
        for position in row:
            if position == "X":
                x_count += 1
            elif position == "O":
                o_count += 1
            elif position != EMPTY:
                raise KeyError("Invalid board")
            
    if x_count - o_count == 1:
        return "O"
    else:
        return "X"


def actions(board) -> set:
    """
    Returns set of all possible actions (i, j) available on the board.

    Input:
        board (list)
    Returns:
        actions (set)
    """
    # initialise actions
    actions = set()

    # initialise i coordinate
    i = 0

    # loop between rows
    for row in board:

        # initialise columns
        j = 0

        # loop through the positions in that row
        for position in row:
            
            # if there is a possible action
            if position == EMPTY:
                actions.add((i, j))
            
            # update coordinate j
            j += 1
        
        # update coordinate i
        i += 1
    
    return actions
            

def result(board, action) -> list:
    """
    Returns the board that results from making move (i, j) on the board.
    If the move is not valid, returns the same board.

    Input:
        board (list)
    Returns:
        virtual_board (list)
    """
    # assign coordinates
    i, j = action

    # create virtual board
    virtual_board = [row.copy() for row in board]

    # raise exception if move is not on the board
    if i < 0 or j < 0 or i > 2 or j > 2:
        raise ValueError("Movement out of bounds")
    
    # modify the matrix adding the correspondant piece
    if virtual_board[i][j] == EMPTY:

        # add the corresponding piece
        virtual_board[i][j] = player(board)
    
    # if move has been made raise error
    else:
        raise ValueError("Move already made")
       
    # return new board
    return virtual_board


def winner(board) -> str:
    """
    Returns the winner of the game, if there is one.

    Input:
        board (list)
    Returns:
        winner (str)
    """
    # check columns to find winner
    winner = check_columns(board)

    # if there is no winner check rows to find winner
    if winner is None:
        winner = check_rows(board)

    # if no winner check diagonals to find winner
    if winner is None:
        winner = check_diagonals(board)

    # return winner
    return winner


def check_columns(board) -> str:
    """
    Checks the columns to find a winner.

    Input:
        board (list)
    Returns:
        winner (str)
    """
    # check the 3 columns
    for col in range(3):

        # if all rows for that column contain "X" return "X"
        if all(board[row][col] == "X" for row in range(3)):
            return "X"
        
        # if all rows for that column contain "O" return "O"
        elif all(board[row][col] == "O" for row in range(3)):
            return "O"
    
    # if no winner return None
    return None


def check_rows(board) -> str:
    """
    Checks the rows to find a winner.

    Input:
        board (list)
    Returns:
        winner (str)
    """
    # check each row on the board
    for row in board:

        # count number of "X". If 3, return "X"
        if row.count("X") == 3:
            return "X"
        
        # count number of "O". If 3, return "O"
        elif row.count("O") == 3:
            return "O"
    
    # if no winner return None
    return None


def check_diagonals(board) -> str:
    """
    Checks the diagonals to find a winner.

    Input:
        board (list)
    Returns:
        winner (str)
    """
    # if all positions in the diagonal are "X" return "X"
    if all(board[i][i] == "X" for i in range(3)) or all(board[i][2 - i] == "X" for i in range(3)):
        return "X"
    
    # if all positions in the diagonal are "O" return "O"
    if all(board[i][i] == "O" for i in range(3)) or all(board[i][2 - i] == "O" for i in range(3)):
        return "O"

    # if no winner return None
    return None


def terminal(board) -> bool:
    """
    Returns True if game is over, False otherwise.

    Input:
        board (list)
    Returns:
        bool
    """
    if winner(board) is not None:
        return True
    
    for row in board:

        for position in row:

            # if there's an empty space return False
            if position == EMPTY:
                return False

    # if there are no empty spaces return True        
    return True        


def utility(board) -> int:
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.

    Input:
        board (list)
    Returns:
        winner of the game (int)
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0


def minimax(board) -> tuple:
    """
    Returns the optimal action for the current player on the board.

    Input:
        board (list)
    Returns:
        action (tuple)
    """
    if terminal(board):
        return None

    elif player(board) == "X":
        _, action = max_value(board)

    else:
        _, action = min_value(board)

    return action


def max_value(board) -> tuple:
    """
    max_value function for the MAX player.

    Input:
        board (list)
    Returns:
        v, best action as a tuple
    """
    # if it's a terminal state, value is taken from utility function
    if terminal(board):
        return utility(board), None
    
    # v = - infinite
    v = float("-inf")

    # initialise best_action
    best_action = None

    # for each possible action
    for action in actions(board):

        # maximise the value of v
        min_val, _ = min_value(result(board, action))

        # if the value can be maximised more update v and best_action
        if min_val > v:
            v = min_val
            best_action = action

    return v, best_action


def min_value(board) -> tuple:
    """
    min_value function for the MIN player.

    Input:
        board (list)
    Returns:
        v, best action (tuple)
    """
    # if it's a terminal state, value is taken from utility function
    if terminal(board):
        return utility(board), None
    
    # v = infinite
    v = float("inf")

    # initialise best_action
    best_action = None

    # for each possible action
    for action in actions(board):

        # minimise value of v
        max_val, _ = max_value(result(board, action))

        # if value is lower than v update v and update best action
        if max_val < v:
            v = max_val
            best_action = action

    return v, best_action