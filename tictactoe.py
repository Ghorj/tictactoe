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

    # modify the matrix adding the correspondant piece
    if virtual_board[i][j] == EMPTY:

        # add the corresponding piece
        virtual_board[i][j] = player(board)
    
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
    winner = check_columns(board)

    if winner == None:
        winner = check_rows(board)

        if winner == None:
            winner = check_diagonals(board)

    return winner


def check_columns(board) -> str:
    """
    Checks the columns to find a winner.

    Input:
        board (list)
    Returns:
        winner (str)
    """
    winner = None
    for i in range(3):

        match = board[0][i]

        if board[1][i] == board[2][i]:

            if board[1][i] == match:

                winner = match
    
    return winner



def check_rows(board) -> str:
    """
    Checks the rows to find a winner.

    Input:
        board (list)
    Returns:
        winner (str)
    """
    winner = None

    for row in board:

        match = row[0]

        if row[1] == row[2]:

            if row[1] == match:

                winner = row[0]

    
    return winner


def check_diagonals(board) -> str:
    """
    Checks the diagonals to find a winner.

    Input:
        board (list)
    Returns:
        winner (str)
    """
    winner = None

    match = board[1][1]

    if board[0][0] == board[2][2]:

        if board[0][0] == match:

            winner = match
    
    elif board[0][2] == board[2][0]:

        if board[0][2] == match:

            winner = match
    
    return winner


def terminal(board) -> bool:
    """
    Returns True if game is over, False otherwise.

    Input:
        board (list)
    Returns:
        bool
    """
    if winner(board) == "X" or winner(board) == "O":
        return True
    
    # loop through board to find None
    else:
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