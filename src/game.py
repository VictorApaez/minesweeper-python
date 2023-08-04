import time
from src.board import Board
class Game:
    def __init__(self, rows, columns, mines):
        self.board = Board(rows, columns, mines)
        self.flags_used = 0
        self.start_time = None 

    def start_game(self):
        self.start_time = time.time()

    def reveal_cell(self, row, column, callback=None):
        if self.start_time is None:
            self.start_game()
            self.board.initialize(row, column)  # place the mines after the first click
        self.board.reveal_cell(row, column, callback)



    def flag_cell(self, row, column):
        cell = self.board.board[row][column]
        if cell.is_flagged:  
            self.flags_used -= 1
        else:
            self.flags_used += 1
        self.board.flag_cell(row, column)
    
    def is_game_over(self):
        return self.board.is_game_over()

    def get_flags_used(self):
        return self.flags_used

    def get_elapsed_time(self):
        if self.start_time is None:
            return 0
        return time.time() - self.start_time
