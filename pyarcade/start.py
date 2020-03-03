import curses
import os

from pyarcade.ui import Menu


def run_pyarcade():
    """ This will effectively become our program entrypoint.
    """
    environ_variables = {"TERM": "linux", "TERMINFO": "/etc/terminfo"}
    os.environ.update(environ_variables)

    screen = curses.initscr()
    main_menu = Menu(screen)
    main_menu.display_main_menu()
    curses.wrapper(run_pyarcade())


def cancel_menu(menu: Menu):
    menu.has_cancel = True


if __name__ == '__main__':
    curses.wrapper(run_pyarcade())
