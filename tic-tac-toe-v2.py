import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title('Tic Tac Toe')
        self.current_player = 'X'
        self.board = [['', '', ''] for _ in range(3)]
        self.game_over = False
        
        # Create the buttons for the game board
        self.buttons = [[tk.Button(self.master, text='', width=10, height=5,
                                    command=lambda row=row, col=col: self.button_click(row, col))
                         for col in range(3)]
                        for row in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].grid(row=row, column=col)
                
        # Create the reset button
        self.reset_button = tk.Button(self.master, text='Reset', width=10, height=2, command=self.reset)
        self.reset_button.grid(row=3, column=1)
        
        # Create the status label
        self.status_label = tk.Label(self.master, text='Player {}\'s turn'.format(self.current_player))
        self.status_label.grid(row=4, column=0, columnspan=3)
        
    def button_click(self, row, col):
        if not self.game_over and self.board[row][col] == '':
            self.buttons[row][col].config(text=self.current_player)
            self.board[row][col] = self.current_player
            if self.check_win():
                self.status_label.config(text='Player {} wins!'.format(self.current_player))
                self.game_over = True
            elif self.check_tie():
                self.status_label.config(text='Tie game!')
                self.game_over = True
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.status_label.config(text='Player {}\'s turn'.format(self.current_player))
                
    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        else:
            return False
        
    def check_tie(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    return False
        return True
                
    def reset(self):
        self.current_player = 'X'
        self.board = [['', '', ''] for _ in range(3)]
        self.game_over = False
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text='')
        self.status_label.config(text='Player {}\'s turn'.format(self.current_player))
        
if __name__ == '__main__':
    root = tk.Tk()
    tictactoe = TicTacToe(root)
    root.mainloop()