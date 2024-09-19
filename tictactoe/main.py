import tkinter as tk
from tkinter import messagebox

# Set up the window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Global variables
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
game_over = False

# Functions
def check_winner():
    """Check if the current player has won."""
    global game_over

    # Check rows, columns, and diagonals
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            highlight_winner(row, 0, row, 1, row, 2)
            game_over = True
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            highlight_winner(0, col, 1, col, 2, col)
            game_over = True 
            return True

    if board[0][0] == board[1][1] == board[2][2] != "":
        highlight_winner(0, 0, 1, 1, 2, 2)
        game_over = True
        return True

    if board[0][2] == board[1][1] == board[2][0] != "":
        highlight_winner(0, 2, 1, 1, 2, 0)
        game_over = True
        return True

    return False

def highlight_winner(row1, col1, row2, col2, row3, col3):
    """Highlight the winning cells."""
    buttons[row1][col1].config(bg="green")
    buttons[row2][col2].config(bg="green")
    buttons[row3][col3].config(bg="green")
    messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")

def check_draw():
    """Check if the game is a draw."""
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                return False
    return True

def handle_click(row, col):
    """Handle button click events."""
    global current_player, game_over

    if not game_over and board[row][col] == "":
        # Mark the board and the button
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        # Check for a winner or draw
        if check_winner():
            return
        elif check_draw():
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            game_over = True
            return

        # Switch players
        current_player = "O" if current_player == "X" else "X"

def reset_game():
    """Reset the game to the initial state."""
    global board, current_player, game_over

    current_player = "X"
    game_over = False
    board = [["" for _ in range(3)] for _ in range(3)]

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="SystemButtonFace")

# Create buttons for the board
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", font=("Arial", 40), width=5, height=2,
                                      command=lambda r=row, c=col: handle_click(r, c))
        buttons[row][col].grid(row=row, column=col)

# Reset button
reset_button = tk.Button(root, text="Restart", font=("Arial", 20), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

# Start the Tkinter event loop
root.mainloop()
