import random


class AI:
    def __init__(self, sign):
        self.sign = sign
        self.name = 'ai'

    def get_name(self):
        return self.name

    @staticmethod
    def get_empty_cells(space):
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


class HardAi(AI):
    def __init__(self, sign):
        super().__init__(sign)
        self.name = 'hard'
        if self.sign == 'X':
            self.enemy_sign = 'O'
        else:
            self.enemy_sign = 'X'

    @staticmethod
    def check_win(space, sign):
        return space[0][0] == sign and space[0][1] == sign and space[0][2] == sign or \
               space[1][0] == sign and space[1][1] == sign and space[1][2] == sign or \
               space[2][0] == sign and space[2][1] == sign and space[2][2] == sign or \
               space[0][0] == sign and space[1][0] == sign and space[2][0] == sign or \
               space[0][1] == sign and space[1][1] == sign and space[2][1] == sign or \
               space[0][2] == sign and space[1][2] == sign and space[2][2] == sign or \
               space[0][0] == sign and space[1][1] == sign and space[2][2] == sign or \
               space[0][2] == sign and space[1][1] == sign and space[2][0] == sign

    @staticmethod
    def min_max(space, sign, player_sign, enemy_sign):
        empty = AI.get_empty_cells(space)
        if HardAi.check_win(space, player_sign):
            return [[-1, -1], 10]
        if HardAi.check_win(space, enemy_sign):
            return [[-1, -1], -10]
        if len(empty) == 0:
            return [[-1, -1], 0]
        moves = list()
        for cell in empty:
            move = list()
            move.append(cell)
            space[cell[0]][cell[1]] = sign
            if sign == player_sign:
                move.append(HardAi.min_max(space, enemy_sign, player_sign, enemy_sign)[1])
            else:
                move.append(HardAi.min_max(space, player_sign, player_sign, enemy_sign)[1])
            space[cell[0]][cell[1]] = ' '
            moves.append(move)
        best_move = []
        if sign == player_sign:
            best_score = -10000
            for mv in moves:
                if mv[1] > best_score:
                    best_score = mv[1]
                    best_move = mv[0]
        else:
            best_score = 10000
            for mv in moves:
                if mv[1] < best_score:
                    best_score = mv[1]
                    best_move = mv[0]
        return [best_move[:], best_score]

    def get_result(self, space):
        space_for_calculate = list()
        for row in space:
            space_for_calculate.append(row[:])

        out = self.min_max(space_for_calculate, self.sign, self.sign, self.enemy_sign)
        return out[0]
