import random
import numpy as np
from copy import deepcopy 

# constants
MAX_BOARD_SIZE = 4

def board_identical(b1, b2):
    for i in range(MAX_BOARD_SIZE):
        for j in range(MAX_BOARD_SIZE):
            if b1[i][j] != b2[i][j]:
                return False
    return True

class board:
    def __init__(self):
        self.board = [[0 for i in range(MAX_BOARD_SIZE)] for j in range(MAX_BOARD_SIZE)]
        self.score = 0
        # self.spawn()

    def spawn(self): # spawn new 1
        empty_coord = random.choice(self.get_empty_coord())
        self.board[empty_coord[0]][empty_coord[1]] = 1

    def move(self, direction):
        # direction: 0 = up, 1 = right, 2 = down, 3 = left
        self.push(direction)

        if direction == 0: # up
            for i in range(MAX_BOARD_SIZE - 1):
                for j in range(MAX_BOARD_SIZE):
                    if self.board[i][j] == self.board[i + 1][j]:
                        self.board[i][j] *= 2
                        self.board[i + 1][j] = 0

                        self.score += self.board[i][j]

        elif direction == 1: # right
            for j in range(MAX_BOARD_SIZE - 1, 0, -1):
                for i in range(MAX_BOARD_SIZE):
                    if self.board[i][j] == self.board[i][j - 1]:
                        self.board[i][j] *= 2
                        self.board[i][j - 1] = 0

                        self.score += self.board[i][j]

        elif direction == 2: # down
            for i in range(MAX_BOARD_SIZE - 1, 0, -1):
                for j in range(MAX_BOARD_SIZE):
                    if self.board[i][j] == self.board[i - 1][j]:
                        self.board[i][j] *= 2
                        self.board[i - 1][j] = 0

                        self.score += self.board[i][j]

        elif direction == 3: # left
            for j in range(MAX_BOARD_SIZE - 1):
                for i in range(MAX_BOARD_SIZE):
                    if self.board[i][j] == self.board[i][j + 1]:
                        self.board[i][j] *= 2
                        self.board[i][j + 1] = 0

                        self.score += self.board[i][j]

        self.push(direction)

    def push(self, direction): # push all blocks to direction
        if direction == 0: # up
            factor = (-1,0)
        elif direction == 1: # right
            factor = (0,1)
        elif direction == 2: # down
            factor = (1,0)
        elif direction == 3: # left
            factor = (0,-1)

        for iteration in range(MAX_BOARD_SIZE):
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] != 0 and (i + factor[0]) in range(len(self.board)) and (j + factor[1]) in range(len(self.board[i])) and self.board[i + factor[0]][j + factor[1]] == 0:
                        self.board[i + factor[0]][j + factor[1]] = self.board[i][j]
                        self.board[i][j] = 0

    def get_empty_coord(self):
        empty_coord = [] # init

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    empty_coord.append((i,j))

        return empty_coord

    def print_board(self):
        print(np.matrix(self.board))
        print("Your score is:", self.score)

    def gameover(self):
        over = False # init

        if not self.get_empty_coord() == []:
            return False

        temp_board = copy.deepcopy(self.board)
        temp_score = copy.deepcopy(self.score)

        self.move(0)
        self.move(1)
        self.move(2)
        self.move(3)

        if board_identical(temp_board, self.board):
            over = True

        self.board = copy.deepcopy(temp_board)
        self.score = copy.deepcopy(temp_score)

        return over

    def grant_point(self, point):
        self.score += point


    def play(self):
        while not self.gameover():
            self.spawn()
            self.print_board()

            old_board = deepcopy(self.board)

            while True:
                print("Please enter direction: ", end='')
                direction = int(input())

                if direction not in [0,1,2,3]:
                    print("Invalid move.")
                    continue
                else:
                    self.move(direction)

                if not board_identical(old_board, self.board):
                    break
                else:
                    print("Invalid move.")
                    continue

            self.grant_point(1)

def main():
    game = board()
    game.play()

main()
