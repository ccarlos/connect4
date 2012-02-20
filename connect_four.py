#!/usr/bin/python

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
        """Construct objects of type GameBoard."""
        self.column_size = column_size
        self.row_size = row_size
        self.data = []

        # Initialize board.
        for r in range(self.row_size):
            board_row = []
            for c in range(self.column_size):
                board_row.append(' ')
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
            board_str += ' ' + str(i % 10)
        board_str += '\n'
        
        return board_str

    def add_piece(self, column, game_piece):
        pass
        # Find the column and insert game_piece. If the lowest slot is taken,
        # go up one level and check again. Do this until the piece is placed.
        # We must check if the column is full prior to placing the piece.

        # After successfully placing piece make a check if the player has won.

game = GameBoard(7, 6)
print game
