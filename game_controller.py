from play_ground import PlayGround
from enum import Enum


class PlayerMode(Enum):
    USER = "user"
    EASY = "easy"


class GameState(Enum):
    MENU = 0
    GAME = 1


class GameController:
    def __init__(self):
        self.pg = PlayGround()
        self.first_mode = PlayerMode.USER
        self.second_mode = PlayerMode.USER
        self.state = GameState.MENU
        self.is_first = True

    def main_menu(self):
        args = input('Input command: ').split()
        if args[0] == 'start':
            if len(args) != 3:
                print('Bad parameters!')
                return
            self.first_mode = PlayerMode(args[1])
            self.second_mode = PlayerMode(args[2])
            self.state = GameState.GAME
            self.is_first = True
            self.pg.clear()
        if args[0] == 'exit':
            exit(0)

    def user_processing(self):
        data_in = input('Enter the coordinates: ').split()
        if len(data_in) == 2:
            coord_y = data_in[0]
            coord_x = data_in[1]
        else:
            print('You should enter numbers!')
            return None
        if not coord_x.isnumeric() or not coord_y.isnumeric():
            print('You should enter numbers!')
            return None
        return [coord_x, coord_y]

    def make_tour(self, mode):
        if mode == PlayerMode.USER:
            if not self.pg.set(*self.user_processing()):
                return False
        if mode == PlayerMode.EASY:
            self.pg.ai_run("easy")
        if self.pg.calculate():
            self.state = GameState.MENU
        return True

    def game(self):
        if self.is_first:
            if self.make_tour(self.first_mode):
                self.is_first = False
        else:
            if self.make_tour(self.second_mode):
                self.is_first = True

    def state_control(self):
        if self.state == GameState.MENU:
            return self.main_menu()
        if self.state == GameState.GAME:
            return self.game()

