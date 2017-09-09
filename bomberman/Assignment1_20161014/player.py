from person import Person
from bomb import Bomb
import sys

class Player(Person):
    '''This class creates an instance of a player. The player can be
    moved around by the user
    '''
    def __init__(self, board):
        '''Creates the player. Player takes board as input for ease of
        updaating information on the board directly
        '''
        #Inherit from Person
        Person.__init__(self, 1, 1)
        #Print onto Board initial location
        board.board[1][1] = "Player"
        self.board = board.board
        self.bombs = 1

    def update_pos(self, direction):
        '''Used to change the position of the player
        '''
        loc = self.get_position()
        x = loc[0]
        y = loc[1]
        #The following are conditions based on direction, to check if
        #the location can be visited by the player. If so, previous player
        #position is erased and updated. If enemy, game over.
        if direction == "Left":
            if self.board[x][y-1] == "Empty":
                self.board[x][y] = "Empty"
                self.board[x][y-1] = "Player"
                self.set_position(x, y-1)
            elif self.board[x][y-1] == "Enemy":
                sys.exit(0)

        elif direction == "Right":
            if self.board [x][y+1] == "Empty":
                self.board[x][y] = "Empty"
                self.board[x][y+1] = "Player"
                self.set_position(x, y+1)
            elif self.board [x][y+1] == "Enemy":
                sys.exit(0)

        elif direction == "Down":
            if self.board [x+1][y] == "Empty":
                self.board[x][y] = "Empty"
                self.board[x+1][y] = "Player"
                self.set_position(x+1, y)
            elif self.board [x+1][y] == "Enemy":
                sys.exit(0)

        elif direction == "Up":
            if self.board [x-1][y] == "Empty":
                self.board[x][y] = "Empty"
                self.board[x-1][y] = "Player"
                self.set_position(x-1, y)
            elif self.board [x-1][y] == "Enemy":
                sys.exit(0)

    def drop_bomb(self):
        '''Controls Number of bombs that can be dropped, by decrementing.
        '''
        if self.bombs > 0:
            self.bombs -= 1
            #Return value shows that a bomb was dropped
            return 1
        else: return 0

    def add_bomb(self):
        '''Used to reset number of bombs
        '''
        self.bombs += 1

    def die(self):
        '''If player dies, game ends
        '''
        sys.exit(0)
