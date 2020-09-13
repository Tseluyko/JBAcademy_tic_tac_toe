import random


class AI:
    def __init__(self, sign):
        self.sign = sign
        self.name = 'ai'

    def get_name(self):
        return self.name

    def get_empty_cells(self, space):
        empty_cells = list()
        for x in range(3):
            for y in range(3):
                if space[x][y] == ' ':
                    empty_cells.append([x, y])
        return empty_cells

    def get_result(self, space):
        pass


class EasyAI(AI):
    def __init__(self, sign):
        super().__init__(sign)
        self.name = 'easy'

    def get_result(self, space):
        cells = self.get_empty_cells(space)
        return cells[random.randint(0, len(cells) - 1)]


class MediumAi(EasyAI):
    def __init__(self, sign):
        super().__init__(sign)
        self.name = 'medium'

    @staticmethod
    def find(space, sign):
        for x in range(3):
            column = space[x]
            if column.count(sign) == 2 and column.count(' ') == 1:
                return [x, column.index(' ')]
        for y in range(3):
            row = [space[x][y] for x in range(3)]
            if row.count(sign) == 2 and row.count(' ') == 1:
                return [row.index(' '), y]
        main = [space[x][x] for x in range(3)]
        if main.count(sign) == 2 and main.count(' ') == 1:
            return [main.index(' '), main.index(' ')]
        side = {(2, 0): space[2][0], (1, 1): space[1][1], (0, 2): space[0][2]}
        sign_count = len([value for key, value in side.items() if value == sign])
        empty_count = len([value for key, value in side.items() if value == ' '])
        if sign_count == 2 and empty_count == 1:
            for key, value in side.items():
                if value == ' ':
                    return key
        return None

    def get_result(self, space):
        win = self.find(space, self.sign)
        if win:
            return win
        if self.sign == 'X':
            danger = self.find(space, 'O')
        else:
            danger = self.find(space, 'X')
        if danger:
            return danger
        return EasyAI.get_result(self, space)
