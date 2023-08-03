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
        #^^ example: 5 mines then 'mines' = a list of 5 random coordinates on the board

        for mine in mines:
            i, j = mine
            self.board[i][j].is_mine = True
    
    def calculate_neighboring_mines(self):
        for i in range(self.rows):
            for j in range(self.columns):
                
                neighbors = []
                #create a 3x3 grid around current cell (inclusive)
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                         # bound check and exclude the current cell (only neighboring cells)
                        if 0 <= x < self.rows and 0 <= y < self.columns and (x, y) != (i, j):
                            neighbors.append((x, y))

                mine_count = 0
                # iterate through neighbors and check if they are mines
                for coords in neighbors:
                    x, y = coords
                    if self.board[x][y].is_mine:
                        mine_count+=1

                self.board[i][j].neighboring_mines = mine_count