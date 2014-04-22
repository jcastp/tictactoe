#!/usr/bin/python3
#
# Simple tic tac toe game

import board

def play():
    print("Playing a game ...")

    # Choose sides

    # Create and initialize the board
    game_board = board.Board()

    # Control of the victory conditions achieved initialized
    victory = False

    # While victory has not been achieved or the board still has 
    # empty places, we keep playing
    while( not victory or game_board.get_empty_spaces != 0):
        # Print the board
        game_board.print_board()

        # A player inserts a piece in the board, taking alternate
        # turns
        # TODO

        # Check victory conditions
        # If victory is achieved by the player, the loop should
        # be interrupted
        victory = True

    
    # Check if the loop has been ended by exausting all the
    # possible spaces
    if not victory:
        print("It's a tie.")
    else:
        print("There is a winner")
    return

if __name__ == "__main__":
    play()
