import tkinter as tk
from src.game import Game
from src.cell import MineRevealedError
from tkinter import messagebox

class MinesweeperGUI:
    def __init__(self, root, rows=9, columns=9, mines=10):
        self.game = Game(rows, columns, mines)
        self.root = root
        self.buttons = [[None for _ in range(columns)] for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                button = tk.Label(root, text="", bg="#90CAF9", relief="raised", height=4, width=4)
                button.bind("<Button-1>", lambda event, row=i, col=j: self.reveal_cell(row, col))
                button.bind("<Button-2>", lambda event, row=i, col=j: self.flag_cell(row, col))
                button.grid(row=i, column=j, sticky="nsew", padx=0, pady=0)
                self.buttons[i][j] = button
        for i in range(rows):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)

    def flag_cell(self, row, col):
        self.game.flag_cell(row, col)
        cell = self.game.board.board[row][col]
        self.update_button_ui(row, col, cell)

    def reveal_cell(self, row, col):
      try:
          self.game.reveal_cell(row, col, self.update_button_ui)
          if self.game.has_won():
              self.end_game()
              self.root.after(100, lambda: messagebox.showinfo("Congratulations", "You Won!"))

      except MineRevealedError:
          self.end_game()
          self.root.after(100, lambda: messagebox.showinfo("Game Over", "Boom! You Lost!")) 


    def update_button_ui(self, row, col, cell):
        button = self.buttons[row][col]
        if cell.is_revealed:
            if cell.is_mine:
                button.config(text="M", bg="#D32F2F")
            else:
                button.config(text=str(cell.neighboring_mines), bg='#A5D6A7')
        elif cell.is_flagged:
            button.config(text="F", bg="#FF9800")
        else:
            button.config(text="", bg="#90CAF9")

    def end_game(self):
        for i in range(self.game.board.rows):
            for j in range(self.game.board.columns):
                if self.game.board.board[i][j].is_mine:
                    self.buttons[i][j].config(text="M", bg="red")


                
            

root = tk.Tk()
root.title("Minesweeper")
gui = MinesweeperGUI(root)
root.mainloop()
