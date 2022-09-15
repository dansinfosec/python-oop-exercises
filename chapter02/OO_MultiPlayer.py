# Consider a game where we have multiple players. A player could be
# modeled by a Player class with instance variables for name , points , health ,
# location , and so on. Each player would have the same capabilities, but
# the methods could work differently based on the different values in the
# instance variables.


class Player(object):
    """docstring for Player"""

    def __init__(self, arg):
        super(Player, self).__init__()
        self.arg = arg
