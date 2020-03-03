import curses

from pyarcade.client import *
from curses import *


class UserInterface:
    def __init__(self, window):
        self.client = Client()
        self.window = window
        curses.start_color()
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE)
        self.show_main_menu()

    def show_main_menu(self):
        menu = ['Hidden Sequence', "Mine Sweeper", "War", "Exit"]
        selected_row = 0
        menu_functions = [self.show_hidden_sequence]

        self.refresh_menu(menu, selected_row)
        self.wait_enter(menu, selected_row, menu_functions)

    def show_hidden_sequence(self):
        menu = ['Hidden Sequence', "Input Here", "Exit"]
        selected_row = 0

        self.refresh_menu(menu, selected_row)
        self.wait_enter(menu, selected_row, [self.show_main_menu])

    def show_text_input(self, prompt: str):
        pass

    def wait_enter(self, menu: [int], selected_row: int, menu_functions_cbs):
        while True:
            key = self.window.getch()

            if key == curses.KEY_UP:
                selected_row = max(0, selected_row - 1)
            elif key == curses.KEY_DOWN:
                selected_row = min(len(menu) - 1, selected_row + 1)
            elif key == curses.KEY_ENTER or key == 10:
                if selected_row == len(menu) - 1:
                    break
                menu_functions_cbs[selected_row]()

            self.refresh_menu(menu, selected_row)

    def refresh_menu(self, menu: [str], selected_row: int):
        self.window.clear()

        for index, item in enumerate(menu):
            if index == selected_row:
                self.window.attron(curses.color_pair(1))
                self.window.addstr(index, 0, item)
                self.window.attroff(curses.color_pair(1))
            else:
                self.window.addstr(index, 0, item)
        self.window.refresh()


if __name__ == '__main__':
    wrapper(UserInterface)



