""" 2048 BackEnd Logic

The idea of this project is to create all 2048 game
in python withou using game libraries, like pygame.
It's a interesting ideia to learn about manipulate
data, logic, algorithms, etc. 
"""

import numpy as np
import random, keyboard, os

class Game2048():
    def __init__(self) -> None:
        self.board = np.zeros((4,4), dtype=int)
        self.round = -2
        self.startGame()

    def drawNewNumbers(self):
        """
        Generates new numbers on the board by selecting a random
        empty cell and assigning a random number from a set of
        possible numbers.

        Parameters:
            self (object): The instance of the class.
        
        Returns:
            None
        """        
        POSSIBLE_NUMS = (2,4)
        NUMS_PROBABILITIES = (0.9, 0.1)
        possibles_coordinate = []

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    possibles_coordinate += [(i,j)]
        
        if possibles_coordinate:
            coordinates = random.choice(possibles_coordinate)
            i,j = coordinates[0], coordinates[1]
            num = np.random.choice(POSSIBLE_NUMS, p=NUMS_PROBABILITIES)
            self.board[i][j] = num
            self.round += 1
            del i,j
        
    def moveUp(self):

        temp = np.array(self.board)

        for i in range(3):
            for i in range(len(self.board)-1):
                for j in range(len(self.board[i])):
                    if self.board[i][j] ==0:
                        self.board[i][j] = self.board[i+1][j]
                        self.board[i+1][j] = 0
        
        for i in range(len(self.board)-1):
            for j in range(len(self.board[i])):
                if self.board[i][j] == self.board[i+1][j]:
                    n = self.board[i][j]
                    self.board[i][j] += self.board[i+1][j]
                    self.board[i+1][j] = 0

        for i in range(3):
            for i in range(len(self.board)-1):
                for j in range(len(self.board[i])):
                    if self.board[i][j] ==0:
                        self.board[i][j] = self.board[i+1][j]
                        self.board[i+1][j] = 0

        temp = np.array(temp) == np.array(self.board)
        
        if temp.all() == True:
            del temp
        
        else:
            self.drawNewNumbers()

    def moveDown(self):

        temp = np.array(self.board)
        
        for i in range(3):
            for i in range(len(self.board)-1, 0, -1):
                for j in range(len(self.board[i])):
                    if self.board[i][j] ==0:
                        self.board[i][j] = self.board[i-1][j]
                        self.board[i-1][j] = 0

        for i in range(len(self.board)-1, 0, -1):
            for j in range(len(self.board[i])):
                if self.board[i][j] == self.board[i-1][j]:
                    self.board[i][j] += self.board[i-1][j]
                    self.board[i-1][j] = 0

        for i in range(3):
            for i in range(len(self.board)-1, 0, -1):
                for j in range(len(self.board[i])):
                    if self.board[i][j] ==0:
                        self.board[i][j] = self.board[i-1][j]
                        self.board[i-1][j] = 0

        temp = np.array(temp) == np.array(self.board)
        
        if temp.all() == True:
            del temp
        
        else:
            self.drawNewNumbers()

    def moveLeft(self):

        temp = np.array(self.board)
        
        for i in range(3):
            for i in range(len(self.board)):
                for j in range(len(self.board[i])-1):
                    if self.board[i][j] ==0:
                        self.board[i][j] = self.board[i][j+1]
                        self.board[i][j+1] = 0

        for i in range(len(self.board)):
            for j in range(len(self.board[i])-1):
                if self.board[i][j] == self.board[i][j+1]:
                    self.board[i][j] += self.board[i][j+1]
                    self.board[i][j+1] = 0

        for i in range(3):
            for i in range(len(self.board)):
                for j in range(len(self.board[i])-1):
                    if self.board[i][j] ==0:
                        self.board[i][j] = self.board[i][j+1]
                        self.board[i][j+1] = 0

        temp = np.array(temp) == np.array(self.board)
        
        if temp.all() == True:
            del temp
        
        else:
            self.drawNewNumbers()

    def moveRight(self):

        temp = np.array(self.board)
        
        for i in range(3):
            for i in range(len(self.board)):
                for j in range(len(self.board[i])-1, 0, -1):
                    if self.board[i][j] ==0:
                        self.board[i][j] = self.board[i][j-1]
                        self.board[i][j-1] = 0

        for i in range(len(self.board)):
            for j in range(len(self.board[i])-1, 0, -1):
                if self.board[i][j] == self.board[i][j-1]:
                    self.board[i][j] += self.board[i][j-1]
                    self.board[i][j-1] = 0

        for i in range(3):
            for i in range(len(self.board)):
                for j in range(len(self.board[i])-1, 0, -1):
                    if self.board[i][j] ==0:
                        self.board[i][j] = self.board[i][j-1]
                        self.board[i][j-1] = 0

        temp = np.array(temp) == np.array(self.board)
        
        if temp.all() == True:
            del temp
        
        else:
            self.drawNewNumbers()

    def gameOver(self):

        temp = Game2048()
        temp.board = np.array(self.board)

        temp.moveLeft()
        temp.moveRight()
        temp.moveUp()
        temp.moveDown()

        temp = temp.board == self.board
        if temp.all() == True:
            print('\n'+'-'*25,f'\n{"Game Over":^25}\n','-'*25,f'\n{f"Rounds: {self.round}":^25}\n', sep='')
            keyboard.press_and_release('esc')
            exit()

        del temp

    def startGame(self):
        self.drawNewNumbers()
        self.drawNewNumbers()

    def clearTerminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')


g = Game2048()
print(g.board)

def on_key_press(key):
    print(key.name)

    MOVES = {
        'up': g.moveUp,
        'left': g.moveLeft,
        'down': g.moveDown,
        'right': g.moveRight,
        'w': g.moveUp,
        'a': g.moveLeft,
        's': g.moveDown,
        'd': g.moveRight,
        'c': g.clearTerminal,
    }
    
    move = MOVES.get(key.name)

    if move:
        move()
        g.clearTerminal()
        print(g.board)
        g.gameOver()

keyboard.on_press(on_key_press)

keyboard.wait('esc')

exit()