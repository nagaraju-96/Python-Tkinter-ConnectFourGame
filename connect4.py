import tkinter as tk
from tkinter import messagebox

class Player:
    def __init__(self, symbol):
        """ Constructor for the Player class"""
        self.symbol = symbol  # Player symbol ('X' or 'O')

class ConnectFour:

    def __init__(self, player1, player2, connect_four_gui):
        """ Constructor for the ConnectFour class"""
        self.board = [[' ' for _ in range(7)] for _ in range(6)]  # Initialize the game board
        self.players = [player1, player2]  # List of player objects
        self.current_player = player1  # Current player
        self.game_over = False  # Game over flag
        self.connect_four_gui = connect_four_gui  # Reference to the GUI

    def update_board_gui(self):
        """ Update the GUI with the current state of the board"""
        self.connect_four_gui.update_board_gui()

    def is_valid_move(self, column):
        """Check if a move is valid in the given column."""
        return self.board[0][column] == ' '

    def drop_piece(self, column):
        """Drop a piece into the specified column."""
        for row in range(5, -1, -1):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player.symbol
                return row, column

    def check_win(self, row, col):
        """Check if the current player has won the game."""
        player_symbol = self.current_player.symbol
        # Check horizontal
        for i in range(3, -1, -1):
            if col - i >= 0 and col - i < 7:
                if self.check_line(row, col - i - 1, 0, 1, player_symbol):
                    return True
        # Check vertical
        if self.check_line(row - 1, col, 1, 0, player_symbol):
            return True
        # Check diagonals
        for i in range(3, -1, -1):
            if col - i >= 0 and col - i < 7:
                if self.check_line(row + i - 1, col - i - 1, 1, 1, player_symbol) or self.check_line(row + i + 1, col - i - 1, -1, 1, player_symbol):
                    return True

        return False

    def check_line(self, row, col, row_delta, col_delta, player_symbol):
        """Check if there is a winning line starting from the given position."""
        for _ in range(4):
            row += row_delta
            col += col_delta
            if not (0 <= row < 6 and 0 <= col < 7) or self.board[row][col] != player_symbol:
                return False

        return True

    def is_board_full(self):
        """Check if the board is full."""
        return all(cell != ' ' for row in self.board for cell in row)

    def switch_player(self):
        """Switch to the other player."""
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def play_game(self, column):
        """Play one move of the game."""
        if not self.game_over:
            if 0 <= column <= 6 and self.is_valid_move(column):
                row, col = self.drop_piece(column)

                # Check if the current player has won
                if self.check_win(row, col):
                    self.update_board_gui()
                    self.game_over = True
                    messagebox.showinfo("Game Over", f"Player {self.current_player.symbol} wins!")
                # Check if the board is full (tie)
                elif self.is_board_full():
                    self.game_over = True
                    messagebox.showinfo("Game Over", "It's a tie!")
                else:
                    self.switch_player()
                    self.update_board_gui()

            else:
                messagebox.showwarning("Invalid Move", "Invalid move. Please choose a valid column (1-7).")


class ConnectFourGUI:
    def __init__(self, root):
        # Constructor for the ConnectFourGUI class
        self.root = root
        self.root.title("Connect Four")

        player1 = Player('X')  # Create Player 1 with symbol 'X'
        player2 = Player('O')  # Create Player 2 with symbol 'O'

        self.game = ConnectFour(player1, player2, self)  # Create a ConnectFour game instance

        self.create_gui()  # Create the GUI elements

    def create_gui(self):
        # Create the GUI elements
        self.buttons = [[None for _ in range(7)] for _ in range(6)]

        for i in range(6):
            for j in range(7):
                player = self.game.players[0] if (i + j) % 2 == 0 else self.game.players[1]
                self.buttons[i][j] = tk.Button(self.root, text='⬇', width=6, height=3, font=("Helvetica", 18), bg='white', command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def update_board_gui(self):
        # Update the GUI with the current state of the board
        color = 'white'
        for i in range(6):
            for j in range(7):
                symbol = self.game.board[i][j]
                if symbol == 'X':
                    color = 'red'
                elif symbol == 'O':
                    color = 'yellow'
                else:
                    symbol = '⬇'
                    color = 'white'
                self.buttons[i][j].config(text=symbol, bg=color)

    def on_button_click(self, row, col):
        # Handle button click event
        self.game.play_game(col)

if __name__ == "__main__":
    root = tk.Tk()
    connect_four_gui = ConnectFourGUI(root)
    root.mainloop()

