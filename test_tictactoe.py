import pytest
from tictactoe import *

def test_initial_state():
    assert initial_state() == [[None, None, None],
            [None, None, None],
            [None, None, None]]
    

def test_player():
    assert player([[None, None, None],
            [None, None, None],
            [None, None, None]]) == "X"
    
    assert player([["X", None, None],
            [None, None, None],
            [None, None, None]]) == "O"
    
    assert player([["O", None, None],
            [None, "X", None],
            [None, None, None]]) == "X"
    
    assert player([["X", "O", "X"],
            [None, "X", None],
            [None, None, "O"]]) == "O"
    
def test_actions():
    assert actions([["X", "O", "X"],
            [None, "X", None],
            [None, None, "O"]]) == {(2, 1), (2, 3), (3, 1), (3, 2)}
    
def test_result():
    assert result([[None, None, None],
            [None, None, None],
            [None, None, None]], (1, 1)) == [["X", None, None],
            [None, None, None],
            [None, None, None]]
    
    assert result([[None, None, None],
            [None, None, None],
            [None, None, None]], (2, 2)) == [[None, None, None],
            [None, "X", None],
            [None, None, None]]
    
    assert result([[None, None, None],
            [None, "X", None],
            [None, None, None]], (1, 1)) == [["O", None, None],
            [None, "X", None],
            [None, None, None]]
    
def test_check_rows():
    assert check_rows([["X", "O", "X"],
            ["X", "X", None],
            ["O", "O", "O"]]) == "O"
    
    assert check_rows([["X", "X", "X"],
            ["X", "O", None],
            ["O", None, "O"]]) == "X"
    
    assert check_rows([["X", "O", "X"],
            ["X", "O", "X"],
            ["O", "X", "O"]]) == None
    
def test_check_columns():
    assert check_columns([["X", "O", "O"],
            ["X", "O", None],
            ["X", None, None]]) == "X"
    
def test_check_diagonals():
    assert check_diagonals([["X", "O", "X"],
            ["O", "X", None],
            ["O", "O", "X"]]) == "X"
    
def test_terminal():
    assert terminal([["X", "O", "X"],
            ["O", "X", None],
            ["O", "O", "X"]]) == True
    
    assert terminal([["O", "X", "X"],
            ["X", "X", "O"],
            ["O", "O", "X"]]) == True
    
    assert terminal([[None, None, None],
            [None, None, None],
            [None, None, None]]) == False