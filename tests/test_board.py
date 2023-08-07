import pytest
from src.board import Board
from src.cell import MineRevealedError
import random

def test_place_mines():
    rows, columns, mines = 5, 5, 5
    board = Board(rows, columns, mines)

    exclude = [(2, 2)]
    random.seed(42)
    board.place_mines(exclude)

    mine_count = sum(cell.is_mine for row in board.board for cell in row)
    assert mine_count == mines

    assert not board.board[exclude[0][0]][exclude[0][1]].is_mine


def test_neighboring_mines_count():
    # no mines
    rows, columns, mines = 5, 5, 0
    board = Board(rows, columns, mines)

    for row in board.board:
        for cell in row:
            assert cell.neighboring_mines == 0, "Expected 0 neighboring mines for an empty board"

    board.board[0][0].is_mine = True
    # ^^ 1 mine at (0,0)
    # [
    #   [x, _, _, _, _],
    #   [_, _, _, _, _],
    #   [_, _, _, _, _],
    #   [_, _, _, _, _],
    #   [_, _, _, _, _]
    # ]
    board.calculate_neighboring_mines()

    # (0, 1), (1, 0) and (1, 1) should each have 1 neighboring mine
    assert board.board[0][1].neighboring_mines == 1, "Expected 1 neighboring mine"
    assert board.board[1][0].neighboring_mines == 1, "Expected 1 neighboring mine"
    assert board.board[1][1].neighboring_mines == 1, "Expected 1 neighboring mine"

    # All other cells should have 0 neighboring mines
    for i in range(rows):
        for j in range(columns):
            if (i, j) not in [(0, 1), (1, 0), (1, 1)]:
                assert board.board[i][j].neighboring_mines == 0, "Expected 0 neighboring mines"

def test_reveal_cell():
    board = Board(5, 5, 5)
    
    cell = board.board[0][0]
    cell.is_mine = False
    board.reveal_cell(0, 0)
    assert cell.is_revealed

    mine_cell = board.board[0][1]
    mine_cell.is_mine = True
    with pytest.raises(MineRevealedError):
        board.reveal_cell(0, 1)

def test_flag_cell():
    board = Board(5, 5, 5)
    cell = board.board[0][0]
    board.flag_cell(0, 0)
    assert cell.is_flagged
    board.flag_cell(0, 0)
    assert not cell.is_flagged

def test_is_game_over_has_won():
    board = Board(3, 3, 1)
    # Reveal all non-mine cells
    for row in range(board.rows):
        for col in range(board.columns):
            if not board.board[row][col].is_mine:
                board.reveal_cell(row, col)
    assert board.is_game_over() == True

def test_is_game_over_mine_revealed():
    board = Board(3, 3, 1)
    board.initialize(0, 0)
    # Triggering a game over by revealing a mine
    mine_revealed = False
    for row in range(board.rows):
        for col in range(board.columns):
            if board.board[row][col].is_mine:
                try:
                    board.reveal_cell(row, col)
                except MineRevealedError:
                    mine_revealed = True
                break
    assert mine_revealed
    assert board.is_game_over() == True

def test_has_won_false():
    board = Board(3, 3, 1)
    assert board.has_won() == False

def test_has_won_true():
    board = Board(3, 3, 1)
    # Reveal all non-mine cells
    for row in range(board.rows):
        for col in range(board.columns):
            if not board.board[row][col].is_mine:
                board.reveal_cell(row, col)
    assert board.has_won() == True