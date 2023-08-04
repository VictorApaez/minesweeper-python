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

root = tk.Tk()
gui = MinesweeperGUI(root)
root.mainloop()
