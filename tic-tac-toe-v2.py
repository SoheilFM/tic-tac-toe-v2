import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.create_widgets()

    def create_widgets(self):
        self.cells = []
        for row in range(3):
            cell_row = []
            for col in range(3):
                cell = tk.Button(self.master, text=" ", font=("Helvetica", 32), width=3, height=1,
                                 command=lambda row=row, col=col: self.on_click(row, col))
                cell.grid(row=row, column=col, sticky="nsew")
                cell_row.append(cell)
            self.cells.append(cell_row)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset)
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def on_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.cells[row][col].configure(text=self.current_player)
            self.current_player = "O" if self.current_player == "X" else "X"
            winner = self.check_winner()
            if winner:
                for cell_row in self.cells:
                    for cell in cell_row:
                        cell.config(state="disabled")
                self.reset_button.config(state="normal")
                tk.messagebox.showinfo("Game Over", f"{winner} wins!")
            elif self.is_board_full():
                for cell_row in self.cells:
                    for cell in cell_row:
                        cell.config(state="disabled")
                self.reset_button.config(state="normal")
                tk.messagebox.showinfo("Game Over", "Tie game!")

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]
        return None

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def reset(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for cell_row in self.cells:
            for cell in cell_row:
                cell.configure(text=" ", state="normal")
        self.reset_button.configure(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()