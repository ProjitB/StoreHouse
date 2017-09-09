import sys
import os
import termios
import fcntl
import tty
import atexit
from select import select

class KBHit():

    def __init__(self):
        '''Creates a KBHit object
        '''
        # Save terminal settings
        self.filedesc = sys.stdin.fileno()
        self.prevTerminal = termios.tcgetattr(self.filedesc)
        self.curTerminal = termios.tcgetattr(self.filedesc)

        # Terminal reset when exit
        atexit.register(self.set_normal_term)

        # Setting new terminal to unbuffered
        self.curTerminal[3] = (self.curTerminal[3] & ~termios.ICANON &
                                   ~termios.ECHO)
        termios.tcsetattr(self.filedesc, termios.TCSAFLUSH, self.curTerminal)

    def set_normal_term(self):
        ''' Resets the terminal
        '''
        termios.tcsetattr(self.filedesc, termios.TCSAFLUSH, self.prevTerminal)

    def getch(self):
        ''' Returns the keyboard character from kbhit()
        '''
        return sys.stdin.read(1)

    def kbhit(self):
        ''' True if character hit, false otherwise
        '''
        dr, dw, de = select([sys.stdin], [], [], 0)
        return dr != []
