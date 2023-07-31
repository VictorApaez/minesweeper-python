import pytest
from src.cell import Cell, MineRevealedError

def test_initial_state():
    cell = Cell()
    assert not cell.is_mine
    assert not cell.is_revealed
    assert not cell.is_flagged
    assert cell.neighboring_mines == 0

def test_reveal_not_mine():
    cell = Cell()
    cell.reveal()
    assert cell.is_revealed

def test_reveal_mine():
    cell = Cell()
    cell.is_mine = True
    with pytest.raises(MineRevealedError):
        cell.reveal()

def test_flag_not_revealed():
    cell = Cell()
    cell.flag()
    assert cell.is_flagged
    cell.flag()
    assert not cell.is_flagged

def test_flag_revealed():
    cell = Cell()
    cell.reveal()
    cell.flag()
    assert not cell.is_flagged

def test_reveal_flagged():
    cell = Cell()
    cell.flag()
    cell.reveal()
    assert not cell.is_revealed
