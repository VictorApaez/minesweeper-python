import pytest
from src.game import Game
from src.cell import MineRevealedError

def test_game():
    game = Game(5, 5, 5)

    assert game.get_flags_used() == 0
    assert game.get_elapsed_time() == 0

    game.flag_cell(0, 0)

    assert game.get_flags_used() == 1

    game.flag_cell(0, 0)

    assert game.get_flags_used() == 0

    game.start_game()

    assert game.get_elapsed_time() >= 0

    cell = game.board.board[0][1]
    cell.is_mine = False
    game.reveal_cell(0, 1)

    cell = game.board.board[0][2]
    cell.is_mine = True
    with pytest.raises(MineRevealedError):
        game.reveal_cell(0, 2)

    assert game.is_game_over()
