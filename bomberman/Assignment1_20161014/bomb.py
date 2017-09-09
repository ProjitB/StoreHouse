import time
import sys
import threading
from threading import *

#Possible states through which the bomb can go through
listTerm = ["Empty", "Bomb0", "Bomb1", "Bomb2", "Bomb3"]

#Things which can be destroyed by a bomb, player included separately
canBomb = ["Empty", "Enemy", "Brick", "Bomb1"]

class Bomb(object):
    def __init__(self, x, y, board):
        '''Initializes the bomb. Sets its location on the board.
        '''
        self.x = x
        self.y = y
        self.board = board.board
        self.boardObj = board
        self.start = time.time()
        self.exploded = 0

    def dropped(self):
            ''' Allows for countdown of bomb. Times 3 seconds till explosion.
            '''
            t = time.time()
            if t - self.start > 4:
                self.exploded1()
            elif t - self.start > 3:
                self.explode()
            elif t -self.start > 2:
                self.explode1()
            elif t - self.start > 1:
                self.explode2()
            elif t - self.start > 0:
                self.explode3()

    def exploded1(self):
        '''Returns 1 if the bomb has exploded. This would imply it needs to be
        cleared from the screen
        '''
        if self.board[self.x][self.y] in listTerm:
            self.exploded = 1

    def explode(self):
        '''The final explosion. If the bomb touches the player, the
        game exits, as the player has died.
        Prints the bomb into the locations around the bomb
        '''
        if self.board[self.x][self.y] in listTerm:
            if self.board[self.x+1][self.y] in canBomb:
                self.board[self.x+1][self.y] = "Bomb0"
            elif self.board[self.x+1][self.y] == "Player":
                sys.exit(0)
            if self.board[self.x][self.y] in canBomb:
                self.board[self.x][self.y] = "Bomb0"
            elif self.board[self.x][self.y] == "Player":
                sys.exit(0)
            if self.board[self.x-1][self.y] in canBomb:
                self.board[self.x-1][self.y] = "Bomb0"
            elif self.board[self.x-1][self.y] == "Player":
                sys.exit(0)
            if self.board[self.x][self.y+1] in canBomb:
                self.board[self.x][self.y+1] = "Bomb0"
            elif self.board[self.x][self.y+1] == "Player":
                sys.exit(0)
            if self.board[self.x][self.y-1] in canBomb:
                self.board[self.x][self.y-1] = "Bomb0"
            elif self.board[self.x][self.y-1] == "Player":
                sys.exit(0)
#The following are for the Countdown

    def explode1(self):
        #Changing state to Bomb1
        if self.board[self.x][self.y] in listTerm:
            self.board[self.x][self.y] = "Bomb1"

    def explode2(self):
        #Changing state to Bomb2
        if self.board[self.x][self.y] in listTerm:
            self.board[self.x][self.y] = "Bomb2"

    def explode3(self):
        #Changing State to Bomb3
        if self.board[self.x][self.y] in listTerm:
            self.board[self.x][self.y] = "Bomb3"
