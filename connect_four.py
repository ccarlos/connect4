class GameBoard:
    """Represents a connect four board.

    Players X and O alternate between turns until a tie or a win.

    Atrributes:
        column_size: Integer representing column size.
        row_size: Integer representing row size.
    """
    EMPTY_SLOT = ' '

    def __init__(self, column_size, row_size):
        """Construct object of type GameBoard."""
        self.column_size = column_size
        self.row_size = row_size
        self.data = []

        # Initialize board.
        for row in range(self.row_size):
            board_row = []
            for col in range(self.column_size):
                board_row.append(GameBoard.EMPTY_SLOT)
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
        for num in range(self.column_size):
            board_str += GameBoard.EMPTY_SLOT + str(num % 10)
        board_str += '\n'

        return board_str

    def add_piece(self, column, game_piece):
        """Add a game piece to game board, given a column and game_piece."""
        for row in reversed(range(self.row_size)):
            # Find first row with an empty slot.
            if self.data[row][column] == GameBoard.EMPTY_SLOT:
                self.data[row][column] = game_piece
                break

    def clear(self):
        """Clears the gameboard of any game pieces intact."""
        for row in range(self.row_size):
            for col in range(self.column_size):
                self.data[row][col] = GameBoard.EMPTY_SLOT

    def set_board(self, moves):
        """Prefill a game board given a string of column numbers."""
        game_piece = 'X'
        for ch in moves:
            column = int(ch)
            if 0 <= column <= self.column_size:
                self.add_piece(column, game_piece)

            game_piece = 'O' if game_piece == 'X' else 'X'

    def column_full(self, column):
        """A column is scanned to determine if there is room available."""
        if self.data[0][column] != GameBoard.EMPTY_SLOT:
            return True
        return False

    def column_empty(self, column):
        """Is the column empty?"""
        if self.data[self.row_size - 1][column] == GameBoard.EMPTY_SLOT:
            return True
        return False

    def legal_move(self, column):
        """A move is legal if it has a valid column and has room available."""
        if column < 0 or column > (self.column_size - 1):
            return False
        if self.column_full(column):
            return False
        return True

    def is_full(self):
        """Is the board full of game pieces?"""
        for col in range(self.column_size):
            if not self.column_full(col):
                return False
        return True

    def rm_piece(self, column):
        """Removes a game piece given a specified column."""
        if self.column_empty(column):
            pass
        else:
            for row in range(self.row_size):
                if self.data[row][column] != GameBoard.EMPTY_SLOT:
                    self.data[row][column] = GameBoard.EMPTY_SLOT
                    break

    def has_won(self, game_piece):
        """Checks if there is four in a row of a given game_piece."""
        # TODO: Ensure we have row and column sizes of >= 4 before calling.

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

        # Check Diagonally: Start at (row_size-1, 0). north-east.
        for row in reversed(range(self.row_size - 3, self.row_size)):
            for col in range(self.column_size - 3):
                if (self.data[row][col] == game_piece and
                self.data[row - 1][col + 1] == game_piece and
                self.data[row - 2][col + 2] == game_piece and
                self.data[row - 3][col + 3] == game_piece):
                    return True

        # Check Diagonally: Start at (0,0). south-west.
        for row in range(self.row_size - 3):
            for col in range(self.column_size - 3):
                if (self.data[row][col] == game_piece and
                self.data[row + 1][col + 1] == game_piece and
                self.data[row + 2][col + 2] == game_piece and
                self.data[row + 3][col + 3] == game_piece):
                    return True

        return False

    def boot_game(self):
        game_piece = 'X'
        print "\nWelcome to connect4!!!"

        while(True):
            print self
            column = raw_input('%s\'s choice: ' % (game_piece))
            try:
                column = int(column)
            except ValueError:
                print "Please enter a valid numeric column choice."
                continue

            if not self.legal_move(column):
                print "Please retry your column number."
                continue

            self.add_piece(column, game_piece)

            if self.has_won(game_piece):
                print "\nYay! %s has won." % (game_piece)
                print self
                break

            if self.is_full():
                print "\nTie: Board is full."
                print self
                break

            game_piece = 'O' if game_piece == 'X' else 'X'


def main():
    game = GameBoard(7, 6)
    game.boot_game()

if __name__ == '__main__':
    main()
