import os
import time
import sys

import colorama
from colorama import Fore, Back, Style

colorama.init()


clear = lambda : os.system('clear')

class Board(object):
    def __init__(self):
        '''Initializes Board and its dimensions
        '''

        board = []
        a = []
        #Size of board is x
        '''There are 3 types of strings on the board: XXXXXX, X X X X X,
and XX      XX
'''
        x = 17
        for i in range(x):
            a.append("Wall")
        b = []
        for i in range(int(x/2)):
            b.append("Wall")
            b.append("Empty")
        b.append("Wall")
        c = []
        c.append("Wall")
        for i in range(x-2):
            c.append("Empty")
        c.append("Wall")
        #Appending the 3 types of lists
        board.append(list(a))
        for i in range(int(x/2)):
            board.append(list(c))
            board.append(list(b))
        board.append(list(c))
        board.append(list(a))
        self.board = board
        self.score = 0
        self.size = x

    def display(self):
        '''Displays the board. Converts the list into string.
        Clears then prints the board.
        Also applies colors while printing.
        '''
        strFinal = ""
        space = " "
        #Conversion to string
        for row in self.board:
            strTemp = ""
            for cell in row:
                if cell == "Wall":
                    strTemp = strTemp + "XXXX"
                elif cell == "Player":
                    strTemp = strTemp + "BBBB"
                elif cell == "Brick":
                    strTemp = strTemp + "////"
                elif cell == "Enemy":
                    strTemp = strTemp + "EEEE"
                elif cell == "Bomb2":
                    strTemp = strTemp +"2222"
                elif cell == "Bomb1":
                    strTemp = strTemp + "1111"
                elif cell == "Bomb0":
                    strTemp = strTemp + "****"
                elif cell == "Bomb3":
                    strTemp = strTemp + "3333"
                else:
                    strTemp = strTemp + 4*space
            strTemp = strTemp + "\n" + strTemp + "\n"
            strFinal = strFinal + strTemp
        clear()
        #printing the string, broken down again to give colors.
        for i in strFinal:
            if i == "X":
                print(Fore.WHITE + i, end = "")
            elif i == "E":
                print(Fore.BLUE + i, end = "")
            elif i == "B":
                print(Fore.YELLOW + i, end = "")
            elif i == "*" or i == "3" or i == "2" or i == "1":
                print(Fore.RED + i, end = "")
            elif i == "/":
                print(Fore.MAGENTA + i, end="")
            else:
                print(Fore.CYAN + i, end = "")
        #printing score
        print("\nScore = " + str(self.score))
#        Alternate: print(strFinal)
