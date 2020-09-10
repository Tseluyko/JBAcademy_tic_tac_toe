# write your code here
import random


class PlayGround:
    def __init__(self, mode):
        self.space = [[' ' for _ in range(3)] for _ in range(3)]
        self.mode = mode

    def set_data(self, x, y, sign):
        if x < 1 or y < 1 or x > 3 or y > 3:
            print('Coordinates should be from 1 to 3!')
            return False
        x -= 1
        y -= 1
        if self.space[x][y] != ' ':
            print('This cell is occupied! Choose another one!')
            return False
        self.space[x][y] = sign
        return True

    def draw(self):
        canvas = f'''---------
| {self.space[2][0]} {self.space[2][1]} {self.space[2][2]} |
| {self.space[1][0]} {self.space[1][1]} {self.space[1][2]} |
| {self.space[0][0]} {self.space[0][1]} {self.space[0][2]} |
---------'''
        print(canvas)

    def set(self, x, y):
        sum_x = len([y for x in self.space for y in x if y == 'X'])
        sum_o = len([y for x in self.space for y in x if y == 'O'])
        sign = 'X'
        if sum_x > sum_o:
            sign = 'O'
        return self.set_data(int(x), int(y), sign)

    def calculate(self):
        if self.space[0][0] == self.space[1][1] == self.space[2][2] == 'X' \
                or self.space[0][2] == self.space[1][1] == self.space[2][0] == 'X':
            print('X wins')
            return True
        if self.space[0][0] == self.space[1][1] == self.space[2][2] == 'O' \
                or self.space[0][2] == self.space[1][1] == self.space[2][0] == 'O':
            print('O wins')
            return True
        if all([x[0] == 'X' for x in self.space]) or \
                all([x[1] == 'X' for x in self.space]) or \
                all([x[2] == 'X' for x in self.space]):
            print('X wins')
            return True
        if all([x[0] == 'O' for x in self.space]) or \
                all([x[1] == 'O' for x in self.space]) or \
                all([x[2] == 'O' for x in self.space]):
            print('O wins')
            return True
        for x in self.space:
            if all([y == 'X' for y in x]):
                print('X wins')
                return True
            if all([y == 'O' for y in x]):
                print('O wins')
                return True
            if any([y == ' ' for y in x]):
                return False

    def ai_easy(self):
        empty_cells = list()
        for x in range(3):
            for y in range(3):
                if self.space[x][y] == ' ':
                    empty_cells.append([x + 1, y + 1])
        random_point = random.randint(0, len(empty_cells) - 1)
        self.set(empty_cells[random_point][0], empty_cells[random_point][1])

    def ai_run(self):
        print('Making move level "{}"'.format(self.mode))
        if self.mode == 'easy':
            return self.ai_easy()


pg = PlayGround("easy")
pg.draw()
coord_x = None
coord_y = None
while True:
    data_in = input('Enter the coordinates: ').split()
    if len(data_in) == 2:
        coord_y = data_in[0]
        coord_x = data_in[1]
    else:
        print('You should enter numbers!')
        continue
    if not coord_x.isnumeric() or not coord_y.isnumeric():
        print('You should enter numbers!')
        continue
    if pg.set(coord_x, coord_y):
        pg.draw()
        if pg.calculate():
            break
    else:
        continue
    pg.ai_run()
    pg.draw()
    if pg.calculate():
        break
