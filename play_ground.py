import random


class PlayGround:
    def __init__(self):
        self.space = self.get_clear_space()

    def clear(self):
        self.space = self.get_clear_space()

    @staticmethod
    def get_clear_space():
        return [[' ' for _ in range(3)] for _ in range(3)]

    def set(self, x, y, sign):
        if self.space[x][y] != ' ':
            print('This cell is occupied! Choose another one!')
            return False
        self.space[x][y] = sign
        self.draw()
        return True

    def draw(self):
        canvas = f'''---------
| {self.space[2][0]} {self.space[2][1]} {self.space[2][2]} |
| {self.space[1][0]} {self.space[1][1]} {self.space[1][2]} |
| {self.space[0][0]} {self.space[0][1]} {self.space[0][2]} |
---------'''
        print(canvas)

    def user_set(self, *args):
        if len(args) != 2:
            return False
        x = int(args[0])
        y = int(args[1])
        if x < 1 or y < 1 or x > 3 or y > 3:
            print('Coordinates should be from 1 to 3!')
            return False
        x -= 1
        y -= 1
        sum_x = len([y for x in self.space for y in x if y == 'X'])
        sum_o = len([y for x in self.space for y in x if y == 'O'])
        sign = 'X'
        if sum_x > sum_o:
            sign = 'O'
        return self.set(x, y, sign)

    def calculate(self):
        if self.space[0][0] == self.space[1][1] == self.space[2][2] == 'X' \
                or self.space[0][2] == self.space[1][1] == self.space[2][0] == 'X':
            print('X wins')
            return True
        if self.space[0][0] == self.space[1][1] == self.space[2][2] == 'O' \
                or self.space[0][2] == self.space[1][1] == self.space[2][0] == 'O':
            print('O wins')
            return True
        for x in range(3):
            if self.space[x].count('X') == 3:
                print('X wins')
                return True
            if self.space[x].count('O') == 3:
                print('O wins')
                return True
        for y in range(3):
            if all([self.space[x][y] == 'X' for x in range(3)]):
                print('X wins')
                return True
            if all([self.space[x][y] == 'O' for x in range(3)]):
                print('O wins')
                return True
        for x in range(3):
            if self.space[x].count(' '):
                return False
        print('Draw')
        return True
