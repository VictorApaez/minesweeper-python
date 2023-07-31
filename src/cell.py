class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.neighboring_mines = 0

    def reveal(self):
        """
        Reveal the cell. If the cell is flagged, nothing happens. If the cell is a mine, a MineRevealedError is raised.
        """
        if self.is_flagged:
            return

        self.is_revealed = True

        if self.is_mine:
            raise MineRevealedError

    def flag(self):
        """
        Flag or unflag the cell. If the cell is already revealed, nothing happens.
        """
        if not self.is_revealed:
            self.is_flagged = not self.is_flagged


class MineRevealedError(Exception):
    """
    Exception raised when a mine is revealed.
    """
    pass
