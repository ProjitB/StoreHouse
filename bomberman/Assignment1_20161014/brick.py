import random
from random import randint

class Brick(object):
    def __init__(self, board):
        '''Initializes the board
        '''
        self.board = board.board
        #Random initial location for Brick
        x = randint(3, board.size)
        y = randint(3, board.size - 1)
        #If original position not allowed:
        while board.board[x][y] != "Empty":
            x = randint(3, board.size - 1)
            y = randint(3, board.size - 1)
        #Printing brick position on the board
        board.board[x][y] = "Brick"
        self.x = x
        self.y = y
