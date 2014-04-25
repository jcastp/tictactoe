## File with the definition of the different IAs' playing
# the game, and their methods

class RandomBot:
    """It plays completely random, without any regard for
    victory conditions, or loosing.
    """
    def __init__(self):
        return


class StatisticsBot:
    """It uses statist tables to determine the best move in
    each turn with pregenerated tables.
    At the beginning of the game, it creates a compillation of
    all the posible moves, and each turn compares the current
    position of the board with a winning position, and determines
    what is the best strategy to win.
    """
    def __init__(self):
        return
