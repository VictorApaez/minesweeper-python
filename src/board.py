from src.cell import Cell 
import random
from src.cell import MineRevealedError

class Board:
    def __init__(self, rows, columns, mines):
        self.rows = rows
        self.columns = columns
        self.mines = mines 
        self.game_over = False
        self.board = [[Cell() for _ in range(columns)] for _ in range(rows)]
        # ^^ 2D array
        # [
        #   [Cell(), Cell(), Cell()]
        #   [Cell(), Cell(), Cell()]
        #   [Cell(), Cell(), Cell()]
        #  ]
        self.mines_placed = False

    def place_mines(self, exclude):
        all_cells = [(i,j) for i in range(self.rows) for j in range(self.columns)]
        all_cells = [cell for cell in all_cells if cell not in exclude]
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

    def initialize(self, row, column):
        if not self.mines_placed:
            neighbors = [(x, y) for x in range(row - 1, row + 2) for y in range(column - 1, column + 2) 
                         if 0 <= x < self.rows and 0 <= y < self.columns]
            self.place_mines(neighbors)
            self.calculate_neighboring_mines()
            self.mines_placed = True

    def reveal_cell(self, row, column, callback=None):
      cell = self.board[row][column]
      try:
          cell.reveal()
      except MineRevealedError:
          self.game_over = True
          raise

      # callback to update UI
      if callback:
          callback(row, column, cell)

      # no neighboring mines
      if cell.neighboring_mines == 0:
          #create a 3x3 grid around current cell (inclusive)
          for r in range(row - 1, row + 2):
              for c in range(column - 1, column + 2):
                  # bound check
                  if 0 <= r < self.rows and 0 <= c < self.columns and not (r == row and c == column):
                      # If a neighboring cell is not already revealed then reveal it
                      if not self.board[r][c].is_revealed:
                          self.reveal_cell(r, c, callback)


 
    def flag_cell(self, row, column):
        self.board[row][column].flag()

    def is_game_over(self):
        # player revealed mine
        if self.game_over or self.has_won():
            return True
        return False        
    
    def has_won(self):
      for row in self.board:
          for cell in row:
              if not cell.is_mine and not cell.is_revealed:
                  return False
      return True
