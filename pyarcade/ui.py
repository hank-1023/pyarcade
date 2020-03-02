import curses
from curses import panel
from os import system
from pyarcade.client import Client
from pyarcade.client import GameType


class Menu(object):

    def __init__(self, stdscreen):
        self.window = stdscreen.subwin(0,0)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()
        self.game = Client()
        self.position = 0

    def navigate(self, n, x):
        self.position += n
        if self.position < 0:
            self.position = 0
        elif self.position >= x:
            self.position = x-1

    def main_menu(self):
        items = ['Play Bull and Cow', 'Play War', 'Play Mine Sweeper', 'Exit']
        self.panel.top()
        self.panel.show()
        self.window.clear()

        while True:
            self.window.refresh()
            curses.doupdate()
            for index, item in enumerate(items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                msg = '%d. %s' % (index, item)
                self.window.addstr(1+index, 1, msg, mode)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                if self.position == 3:
                    break
                else:
                    if self.position == 0:
                        self.bull_and_cow_user_infterface()

            elif key == curses.KEY_UP:
                self.navigate(-1, 4)

            elif key == curses.KEY_DOWN:
                self.navigate(1, 4)

        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()

    def bull_and_cow_user_infterface(self):
        menu = [ 'Bulls and Cows',
                 'My guess:', 'Exit']
        self.panel.top()
        self.panel.show()
        self.window.clear()
        self.game.start_game(GameType.HIDDEN_SEQUENCE)
        while True:
            self.window.refresh()
            curses.doupdate()
            for index, item in enumerate(menu):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                msg = '%d. %s' % (index, item)
                self.window.addstr(1 + index, 1, msg, mode)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                if self.position == 2:
                    break
                elif self.position == 1:
                    key2 = self.window.getch()
                    curses.echo()
                    user_input = self.window.getstr(2, 13)
                    self.window.addstr(2, 13, user_input)
                    if key2 == curses.KEY_ENTER:
                        self.game.parse_execute_input(user_input)
                        self.window.addstr(7, 3, "fuck you")
                        self.window.addstr(7, 3, self.game.get_display_data())
            elif key == curses.KEY_UP:
                self.navigate(-1, 3)

            elif key == curses.KEY_DOWN:
                self.navigate(1, 3)

        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()
        self.main_menu()


class MyApp(object):

    def __init__(self, stdscreen):
        self.screen = stdscreen
        curses.curs_set(0)

        main_menu = Menu(self.screen)
        main_menu.main_menu()


if __name__ == '__main__':
    curses.wrapper(MyApp)








