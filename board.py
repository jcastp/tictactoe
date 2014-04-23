## Class that describes the tic tac toe board

class Board:
    """Description of the tictactoe board, and its functions
    """
    def __init__(self):
        """Initialize the board"""
        self.pieces = [[None, None, None],
                       [None, None, None],
                       [None, None, None]]
        return


    def print_board(self):
        """Converts the layout of the board in a human readable
        format.
        """
        # TODO
        for i in range(len(self.pieces)):
            row_print= ""
            for j in range(len(self.pieces[i])):
                if self.pieces[i][j] is None:
                    print_char = " "
                elif self.pieces[i][j] is True:
                    print_char = "O"
                elif self.pieces[i][j] is False:
                    print_char = "X"
                row_print += print_char
            print(row_print)
            print('\n')
            print('-+-+-')
        return


    def insert_piece(self, side, row, col):
        """Given a side, and a pair of row and column number,
        inserts the piece in the given coordinates.
        """
        self.pieces[row][col] = side
        return


    def get_empty_spaces(self):
        """Returns the number of empty spaces in the
        board."""
        spaces = 0
        for i in range(len(self.pieces)):
            for j in range(len(self.pieces[i])):
                if self.pieces[i][j] == None:
                    spaces += 1
        return spaces
