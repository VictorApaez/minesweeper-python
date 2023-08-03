import pytest
from src.board import Board

def test_mine_placement():
    rows, columns, mines = 5, 5, 5
    board = Board(rows, columns, mines)

    mine_count = sum(cell.is_mine for row in board.board for cell in row)

    assert mine_count == mines, f"Expected {mines} mines, but got {mine_count}"

