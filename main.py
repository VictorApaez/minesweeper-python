import tkinter as tk
from src.game import Game
from src.cell import MineRevealedError

class MinesweeperGUI:
    def __init__(self, root, rows=10, columns=10, mines=30):
        self.game = Game(rows, columns, mines)
        self.root = root
        self.buttons = [[None for _ in range(columns)] for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                button = tk.Label(root, text="", bg="white", relief="raised", height=4, width=4)
                button.bind("<Button-1>", lambda event, row=i, col=j: self.reveal_cell(row, col))
                button.bind("<Button-2>", lambda event, row=i, col=j: self.flag_cell(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button
                
    def flag_cell(self, row, col):
        self.game.flag_cell(row, col)
        cell = self.game.board.board[row][col]
        self.update_button_ui(row, col, cell)

    def reveal_cell(self, row, col):
        try:
            self.game.reveal_cell(row, col, self.update_button_ui)
        except MineRevealedError:
            self.end_game()

    def update_button_ui(self, row, col, cell):
        button = self.buttons[row][col]
        if cell.is_revealed:
            if cell.is_mine:
                button.config(text="M", bg="red")
            else:
                button.config(text=str(cell.neighboring_mines), bg='blue')
        elif cell.is_flagged:
            button.config(text="F", bg="orange")
        else:
            button.config(text="", bg="white")

    def end_game(self):
        for i in range(self.game.board.rows):
            for j in range(self.game.board.columns):
                if self.game.board.board[i][j].is_mine:
                    self.buttons[i][j].config(text="M", bg="red")

root = tk.Tk()
gui = MinesweeperGUI(root)
root.mainloop()
