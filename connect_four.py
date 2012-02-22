#!/usr/bin/python


EMPTY_SLOT = ' '


class Player:
    def __init__(self, name, score, game_piece):
        self.name = name
        self.score = score
        self.game_piece = game_piece


class GamePiece:
    def __init__(self, piece_char, piece_color):
        self.piece_char = piece_char  # An 'x' or 'o'
        self.piece_color = piece_color


class GameBoard:
    def __init__(self, column_size, row_size):
        """Construct object of type GameBoard."""
        self.column_size = column_size
        self.row_size = row_size
        self.data = []

        # Initialize board.
        for r in range(self.row_size):
            board_row = []
            for c in range(self.column_size):
                board_row.append(EMPTY_SLOT)
            self.data.append(board_row)

    def __repr__(self):
        """Return a string representation of an object of type Gameboard."""
        board_str = '\n'
        for row in range(self.row_size):
            board_str += '|'
            for col in range(self.column_size):
                board_str += self.data[row][col] + '|'
            board_str += '\n'

        # Print out the vertical line for board.
        board_str += self.column_size * '--' + '-\n'

        # Print out column numbers, using mod 10 (for spacing issues).
        for i in range(self.column_size):
            board_str += EMPTY_SLOT + str(i % 10)
        board_str += '\n'

        return board_str

    def add_piece(self, column, game_piece):
        """Add a game piece to game board, given a column and game_piece."""
        for row in reversed(range(self.row_size)):
            # Find first row with an empty slot.
            if self.data[row][column] == EMPTY_SLOT:
                self.data[row][column] = game_piece
                break

    def clear(self):
        """Clears the gameboard of any game pieces intact."""
        for row in range(self.row_size):
            for col in range(self.column_size):
                self.data[row][col] = EMPTY_SLOT

    def set_board(self, move_string):
        """Prefill a game board given a string of integers."""
        game_piece = 'X'
        for ch in move_string:
            column = int(ch)
            if 0 <= column <= self.column_size:
                self.add_piece(column, game_piece)

            game_piece = 'O' if game_piece == 'X' else 'X'

    def column_full(self, column):
        """A column is scanned to determine if there is room available."""
        if self.data[0][column] != EMPTY_SLOT:
            return True
        return False

    def column_empty(self, column):
        """Is the column empty?"""
        # Check the lowest row to determined if a game piece exists.
        if self.data[self.row_size - 1][column] == EMPTY_SLOT:
            return True
        return False

    def legal_move(self, column):
        """A move is legal if it has a valid column and has room available."""
        if column < 0 or column > self.column_size:
            return False
        if self.column_full(column):
            return False
        return True

    def is_full(self):
        """Is the board full of game pieces?"""
        for col in range(self.column_size):
            if self.column_full(col):
                return False
        return True

    def rm_piece(self, column):
        """Removes a game piece given a specified column."""
        if self.column_empty(column):
            pass
        else:
            for row in range(self.row_size):
                if self.data[row][column] != EMPTY_SLOT:
                    self.data[row][column] = EMPTY_SLOT
                    break

    def has_won(self, game_piece):
        """Checks if a given game_piece has won. Hor, Ver, Diag."""
        # TODO: Ensure we have row and column sizes of >= 4.

        # Check Horizontally. Start check at lowest row.
        for row in reversed(range(self.row_size)):
            for col in range(self.column_size - 3):
                if (self.data[row][col] == game_piece and
                self.data[row][col + 1] == game_piece and
                self.data[row][col + 2] == game_piece and
                self.data[row][col + 3] == game_piece):
                    return True

        # Check Vertically. Start check at lowest row.
        for col in range(self.column_size):
            for row in reversed(range(self.row_size - 3)):
                if (self.data[row][col] == game_piece and
                self.data[row + 1][col] == game_piece and
                self.data[row + 2][col] == game_piece and
                self.data[row + 3][col] == game_piece):
                    return True

        # Check Diagonally: NE. Start at (row_size-1, 0).
        for row in reversed(range(self.row_size - 3, self.row_size)):
            for col in range(self.column_size - 3):
                if (self.data[row][col] == game_piece and
                self.data[row - 1][col + 1] == game_piece and
                self.data[row - 2][col + 2] == game_piece and
                self.data[row - 3][col + 3] == game_piece):
                    return True

        # Check Diagonally: NS. Start at (0,0).
        for row in range(self.row_size - 3):
            for col in range(self.column_size - 3):
                if (self.data[row][col] == game_piece and
                self.data[row + 1][col + 1] == game_piece and
                self.data[row + 2][col + 2] == game_piece and
                self.data[row + 3][col + 3] == game_piece):
                    return True

        return False

# Debug purposes.
game = GameBoard(7, 6)
game.set_board('2334454551555')

print game

print 'wins for X', game.has_won('X')
print 'wins for O', game.has_won('O')
