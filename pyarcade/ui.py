import curses
from pyarcade.client import *


class MENUTYPE(Enum):

    MAIN_MENU = ['Play Hidden Sequence', 'Play War', 'Play Mine Sweeper', 'Try to Play Games!', 'Exit']
    HIDDENSEQUENCE = ['Hidden Sequence', 'Reset', 'My guess:', 'Exit']
    WAR = ['War', 'Reset', 'Play', 'Exit']
    MINE_SWEEPER = ['Mine Sweeper', 'Reset', 'My move', 'Exit']


class Menu(object):

    def __init__(self, stdscreen):
        self.window = stdscreen.subwin(0, 0)
        self.window.keypad(1)
        self.client = Client()
        self.position = 0

    def move(self, n, x):
        self.position += n
        if self.position < 0:
            self.position = 0
        if self.position >= x:
            self.position = x - 1

    def display_menu(self, client):
        self.window.refresh()
        curses.doupdate()
        for index, item in enumerate(client.value):
            if index == self.position:
                mode = curses.A_REVERSE
            else:
                mode = curses.A_NORMAL
            self.window.addstr(1 + index, 1, item, mode)

    def display_main_menu(self):
        self.window.clear()
        self.position = 0
        while True:
            self.display_menu(MENUTYPE.MAIN_MENU)

            key = self.window.getch()
            self.window.addstr(8, 0, str(self.position))
            if key in [curses.KEY_ENTER, ord('\n')]:
                self.window.addstr(8, 8, str(self.position))
                if self.position == 4:
                    break
                if self.position == 0:
                    self.hidden_sequence_user_interface()
                elif self.position == 1:
                    self.war_menu_interface()
                elif self.position == 2:
                    self.mine_sweeper_interface()
            elif key == curses.KEY_UP:
                self.move(-1, 5)

            elif key == curses.KEY_DOWN:
                self.move(1, 5)

        self.window.clear()
        curses.doupdate()

    def war_menu_interface(self):
        self.window.clear()
        self.client.start_game(GameType.WAR)
        self.position = 0
        while True:
            self.display_menu(MENUTYPE.WAR)
            self.window.addstr(1, 10, "This is a Card Game and you won by getting all the cards from the dealer, "
                                      "each time you will put down one card from top of your stack to compare"
                                      "One with the greater value take all the cards")
            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                if self.position == 3:
                    break
                elif self.position == 2:
                    self.client.parse_execute_input("deal")
                    self.window.addstr(5, 1, self.client.get_display_data())
                elif self.position == 1:
                    self.client.parse_execute_input("reset")
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
        self.client.start_game(GameType.MINE_SWEEPER)
        self.position = 0
        while True:
            self.display_menu(MENUTYPE.MINE_SWEEPER)
            self.window.addstr(1, 10, "This is a Mine Sweeper Game, all you need to do is enter your move and input 1  "
                                      "digit followed by "" "
                                      "One with the greater value take all the cards")

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                if self.position == 3:
                    break
                elif self.position == 2:
                    user_input = self.get_user_input()
                    self.window.addstr(3, 13, user_input)
                    self.client.parse_execute_input(user_input)
                    self.window.addstr(5, 1, self.client.get_display_data())
                elif self.position == 1:
                    self.client.parse_execute_input("reset")
                    self.window.clear()
                    self.window.addstr(10, 1, "You Reset the Game!")

            elif key == curses.KEY_UP:
                self.move(-1, 4)

            elif key == curses.KEY_DOWN:
                self.move(1, 4)

        self.window.clear()
        curses.doupdate()
        self.display_main_menu()

    def hidden_sequence_user_interface(self):
        self.window.clear()
        self.client.start_game(GameType.HIDDEN_SEQUENCE)
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
                    self.client.parse_execute_input(user_input)
                    self.window.addstr(5, 1, self.client.get_display_data())
                elif self.position == 1:
                    self.client.parse_execute_input("reset")
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

    def exit(self):
        curses.endwin()
