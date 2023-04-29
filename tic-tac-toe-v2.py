from tkinter import *
from tkinter import messagebox

# Initialize a 3x3 matrix to represent the Tic Tac Toe board
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

# Initialize player X to go first
current_player = 'X'

# Function to check if there is a winner
def check_winner():
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return board[row][0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    # Check if there is a tie
    if all([all(row) for row in board]):
        return 'Tie'
    # No winner yet
    return None

# Function to handle a player clicking on a cell
def cell_clicked(row, col):
    global current_player
    # Check if the cell is already occupied
    if board[row][col] != '':
        messagebox.showerror('Error', 'This cell is already occupied.')
        return
    # Update the board and the label
    board[row][col] = current_player
    buttons[row][col].config(text=current_player)
    # Check if there is a winner
    winner = check_winner()
    if winner is not None:
        if winner == 'Tie':
            messagebox.showinfo('Game Over', 'It is a tie!')
        else:
            messagebox.showinfo('Game Over', f'{winner} wins!')
        # Reset the game
        reset_game()
        return
    # Switch to the other player
    current_player = 'O' if current_player == 'X' else 'X'
    # Update the turn label
    turn_label.config(text=f"{current_player}'s turn")

# Function to reset the game
def reset_game():
    global board, current_player, turn_label
    board = [['', '', ''],
             ['', '', ''],
             ['', '', '']]
    current_player = 'X'
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text='')
    # Update the turn label
    turn_label.config(text=f"{current_player}'s turn")

    # Create the turn label
    turn_label = Label(root, text=f"{current_player}'s turn")
    turn_label.grid(row=3, column=0, columnspan=3)

# Create the main window
root = Tk()
root.title('Tic Tac Toe')

# Create the buttons for the cells
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = Button(root, text='', width=10, height=5, command=lambda r=row, c=col: cell_clicked(r, c))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

# Create the reset button
reset_button = Button(root, text='Reset', command=reset_game)
reset_button.grid(row=4, column=1)

# Create the turn label
turn_label = Label(root, text=f"{current_player}'s turn")
turn_label.grid(row=3, column=0, columnspan=3)

# Start the game
root.mainloop()