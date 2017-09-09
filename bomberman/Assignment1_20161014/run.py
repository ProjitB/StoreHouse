import readchar
import time
from multiprocessing import Process
import threading
import sys
from threading import *
from board import Board
from person import Person
from player import Player
from bomb import Bomb
from kbhit import KBHit
from enemy import Enemy
from brick import Brick
#Enemy List
eList = []
#Fast Enemy List
eListF = []
#Bombs globally present(restricted to 1)
g_bomb = []

def func2(pos):
    '''This function checks if a bomb is already present on screen. If not
    drops another bomb at the player's position
    '''
    if g_bomb:
        pass
    else:
        #Creating bomb instance
        bomb = Bomb(pos[0], pos[1], a)
        g_bomb.append(bomb)


def func1(temp):
    '''Input is character passed; Movement done based on that
    '''
    if temp == "w":
        c.update_pos("Up")
    elif temp == "a":
        c.update_pos("Left")
    elif temp == "s":
        c.update_pos("Down")
    elif temp == "d":
        c.update_pos("Right")
    elif temp == "b":
        #Checks if player can drop a bomb
        if c.drop_bomb() > 0:
            pos = c.get_position()
            func2(pos)
    #Ends game on pressing q
    elif temp == "q":
        sys.exit(0)
    else:
        pass

def Enemy_move(tprev):
    '''Checks current time difference; If > 1, enemy moves and prev time updated
    '''
    curTime = time.time()
    if curTime - tprev > 1:
        killed = 0
        #If return value from any enemy is > 0 , killed > 0.
        for i in eList:
            killed += i.update_pos()
        tprev = curTime
        #Killed implies player died
        if killed:
            sys.exit(0)
    return tprev

def Enemy_move_fast(tprev):
    '''Checks current time difference; If > 1, enemy moves and prev time updated
    '''
    curTime = time.time()
    if curTime - tprev > 0.3:
        killed = 0
        #If return value from any enemy is > 0 , killed > 0.
        for i in eListF:
            killed += i.update_pos()
        tprev = curTime
        if killed:
        #Killed implies enemy died
            sys.exit(0)
    return tprev


if __name__ == "__main__":
    '''Driving function for the game, has infinite while True loop.
    '''

    #Create Board
    a = Board()
    #Create Player
    c = Player(a)

    #Controls number of Enemies
    numSlowEnemies = 2
    numFastEnemies = 2
    #Controling number of Bricks
    numBricks = 15

    #Creating the Bricks
    for i in range(numBricks):
        b = Brick(a)
    #Creating the Fast enemies
    for i in range(numFastEnemies):
        e = Enemy(a)
        eListF.append(e)
    #Creating the Slow Enemies
    for i in range(numSlowEnemies):
        e = Enemy(a)
        eList.append(e)
    #Inititializing times to calculate movement for slow and fast enemies
    prevTime = time.time()
    prevTimeF = time.time()
    #First print of board
    a.display()
    kb = KBHit()
    while True:
        #Checking Score
        curBricks = 0
        curEnemies = 0
        for x in a.board:
            for cell in x:
                if cell == "Enemy":
                    curEnemies += 1
                elif cell == "Brick":
                    curBricks += 1
        a.score = (numSlowEnemies + numFastEnemies - curEnemies) * 50 + (numBricks - curBricks) * 10
        #Checking if there was an Input, if not go to else statement
        if kb.kbhit():
            ctemp = kb.getch()
            func1(ctemp)
        else:
            #Bomb Exploding
            if g_bomb:
                if g_bomb[0].exploded:
                    #Bomb Countdown
                    a.board[g_bomb[0].x][g_bomb[0].y] = "Empty"
                    if a.board[g_bomb[0].x+1][g_bomb[0].y] == "Bomb0":
                        a.board[g_bomb[0].x+1][g_bomb[0].y] = "Empty"
                    if a.board[g_bomb[0].x-1][g_bomb[0].y] == "Bomb0":
                        a.board[g_bomb[0].x-1][g_bomb[0].y] = "Empty"
                    if a.board[g_bomb[0].x][g_bomb[0].y+1] == "Bomb0":
                        a.board[g_bomb[0].x][g_bomb[0].y+1] = "Empty"
                    if a.board[g_bomb[0].x][g_bomb[0].y-1] == "Bomb0":
                        a.board[g_bomb[0].x][g_bomb[0].y-1] = "Empty"

                    del g_bomb[0]
                    #Player gets another bomb once explosion
                    c.add_bomb()

                else:
                    g_bomb[0].dropped()
            #Enemy Movement
            prevTime = Enemy_move(prevTime)
            prevTimeF = Enemy_move_fast(prevTimeF)
            #Sleep so that board doesn't blink from too fast printing
            time.sleep(0.07)
            a.display()
