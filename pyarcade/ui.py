import curses
from enum import Enum
from pyarcade.client import Client
from pyarcade.client import GameType


class MENUTYPE(Enum):
    MAIN_MENU = ['Play Hidden Sequence', 'Play War', 'Play Mine Sweeper', 'Exit']
    HIDDENSEQUENCE = [ 'Bulls and Cows', 'Reset', 'My guess:', 'Exit']
    WAR = ['War','Reset', 'Play',  'Exit']
    MINE_SWEEPER = ['Mine Sweeper', 'Reset', 'My move', 'Exit']


class Menu(object):

    def __init__(self, stdscreen):
        self.window = stdscreen.subwin(0,0)
        self.window.keypad(1)
        self.game = Client()
        self.position = 0

    def move(self, n, x):
        self.position += n
        if self.position < 0:
            self.position = 0
        elif self.position >= x:
            self.position = x-1

    def display_menu(self, game):
        self.window.refresh()
        curses.doupdate()
        for index, item in enumerate(game.value):
            if index == self.position:
                mode = curses.A_REVERSE
            else:
                mode = curses.A_NORMAL
            self.window.addstr(1 + index, 1, item, mode)

    def display_main_menu(self):
        self.window.clear()
        while True:
            self.display_menu(MENUTYPE.MAIN_MENU)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                if self.position == 3:
                    break
                else:
                    if self.position == 0:
                        self.hidden_sequence_infterface()
                    elif self.position == 1:
                        self.war_menu_interface()
                    elif self.position == 2:
                        self.mine_sweeper_interface()

            elif key == curses.KEY_UP:
                self.move(-1, 4)

            elif key == curses.KEY_DOWN:
                self.move(1, 4)

        self.window.clear()
        curses.doupdate()

    def war_menu_interface(self):
        self.window.clear()
        self.game.start_game(GameType.WAR)
        self.position = 0
        while True:
            self.display_menu(MENUTYPE.WAR)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                if self.position == 3:
                    break
                elif self.position == 2:
                    self.game.parse_execute_input("deal")
                    self.window.addstr(5, 1, self.game.get_display_data())
                elif self.position == 1:
                    self.game.parse_execute_input("reset")
                    self.window.clear()
                    self.window.addstr(5, 1, "You Reset the Game!")

            elif key == curses.KEY_UP:
                self.move(-1, 4)

            elif key == curses.KEY_DOWN:
                self.move(1, 4)

        self.window.clear()
        curses.doupdate()
        self.display_main_menu()

    def mine_sweeper_interface(self):
        self.window.clear()
        self.game.start_game(GameType.MINE_SWEEPER)
        self.position = 0
        while True:
            self.display_menu(MENUTYPE.MINE_SWEEPER)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                if self.position == 3:
                    break
                elif self.position == 2:
                    user_input = self.get_user_input()
                    self.window.addstr(3, 13, user_input)
                    self.game.parse_execute_input(user_input)
                    self.window.addstr(5, 1, self.game.get_display_data())
                elif self.position == 1:
                    self.game.parse_execute_input("reset")
                    self.window.clear()
                    self.window.addstr(10, 1, "You Reset the Game!")

            elif key == curses.KEY_UP:
                self.move(-1, 4)

            elif key == curses.KEY_DOWN:
                self.move(1, 4)

        self.window.clear()
        curses.doupdate()
        self.display_main_menu()

    def hidden_sequence_user_infterface(self):
        self.window.clear()
        self.game.start_game(GameType.HIDDEN_SEQUENCE)
        self.position = 0

        while True:
            self.display_menu(MENUTYPE.HIDDENSEQUENCE)
            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                if self.position == 3:
                    break
                elif self.position == 2:
                    user_input = self.get_user_input()
                    self.window.addstr(3, 13, user_input)
                    self.game.parse_execute_input(user_input)
                    self.window.addstr(5, 1, self.game.get_display_data())
                elif self.position == 1:
                    self.game.parse_execute_input("reset")
                    self.window.clear()
                    self.window.addstr(5, 1, "You Reset the Game!")

            elif key == curses.KEY_UP:
                self.move(-1, 4)

            elif key == curses.KEY_DOWN:
                self.move(1, 4)
        self.window.clear()
        curses.doupdate()
        self.display_main_menu()

    def get_user_input(self):
        self.window.clear()
        i = 0
        user_input = ""
        while True:
            self.window.refresh()
            curses.doupdate()
            self.window.addstr(0, 0, "Press q to Start Play !")
            key = chr(self.window.getch())

            if key in ['q']:
                break
            elif ord(key) != 10:
                self.window.addstr(1, i, key)
                i += 2
                user_input += str(key)

        self.window.clear()
        curses.doupdate()
        return user_input

"""
class MyApp(object):

    def __init__(self, stdscreen):
        self.screen = stdscreen
        curses.curs_set(0)
        main_menu = Menu(self.screen)
        main_menu.display_main_menu()


if __name__ == '__main__':
    curses.wrapper(MyApp)
    """








