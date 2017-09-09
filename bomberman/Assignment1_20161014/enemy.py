from person import Person
import random
from random import randint

class Enemy(Person):
    def __init__(self, board):
        '''Initializing the Enemy
        '''
        self.board = board.board
        #Putting initial possible location for enemy
        x = randint(4, board.size - 2)
        y = randint(4, board.size - 2)
        #If inintial locations are not allowed:
        while board.board[x][y] != "Empty":
            x = randint(4, board.size - 2)
            y = randint(4, board.size - 2)
        #Inheriting from person:
        Person.__init__(self, x, y)
        board.board[x][y] = "Enemy"
        self.x = x
        self.y = y

    def update_pos(self):
        '''Used to change position of the enemy
        Its return value determines if it kills a player in its move
        '''

        #Locations to which the enemy allowed to move to:
        Allowed = ["Empty", "Player"]

        #List of possible locations
        possible = []

        #Checking if enemy exists on board(not bombed)
        #Then putting possible next locations into possible[]
        if self.board[self.x][self.y] == "Enemy":
            if self.board[self.x+1][self.y] in Allowed:
                possible.append([self.x+1, self.y])
            if self.board[self.x-1][self.y] in Allowed:
                possible.append([self.x-1, self.y])
            if self.board[self.x][self.y+1] in Allowed:
                possible.append([self.x, self.y+1])
            if self.board[self.x][self.y-1] in Allowed:
                possible.append([self.x, self.y-1])
            if len(possible) == 0: #If no possible location(enemy trapped)
                return False
            else:
                #Randomly chosing next position
                position = randint(0, len(possible)-1)
                oldx = self.x
                oldy = self.y
                #Assigning new position
                self.x = possible[position][0]
                self.y = possible[position][1]
                #Clearing print Old position
                self.board[oldx][oldy] = "Empty"
                killed = False
                #checking if Player dies
                if self.board[self.x][self.y] == "Player":
                    killed = True
                else:
                    #Printing enemy into new location
                    self.board[self.x][self.y] = "Enemy"

                return killed
        else:
            #If enemy was already dead, it can't kill player so return False
            return False
