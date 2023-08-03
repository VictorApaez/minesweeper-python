from src.cell import Cell 
import random

class Board:
    def __init__(self, rows, columns, mines):
        self.rows = rows
        self.columns = columns
        self.mines = mines 
        self.board = [[Cell() for _ in range(columns)] for _ in range(rows)]
        # ^^ 2D array
        # [
        #   [Cell(), Cell(), Cell()]
        #   [Cell(), Cell(), Cell()]
        #   [Cell(), Cell(), Cell()]
        #  ]
        self.place_mines()
        self.calculate_neighboring_mines()

    def place_mines(self):
        all_cells = [(i,j) for i in range(self.rows) for j in range(self.columns)]
        mines = random.sample(all_cells, self.mines)
        #^^ if 5 mines then mines = a list of 5 random coordinates on the board

        for mine in mines:
            i, j = mine
            self.board[i][j].is_mine = True
    
