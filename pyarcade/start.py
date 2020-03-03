import curses
from pyarcade.ui import Menu
import os

def run_pyarcade():
    """ This will effectively become our program entrypoint.
    """
    environ_var = {"TERM": "linux", "TERMINFO": "/etc/terminfo"}
    os.environ.update(environ_var)

    screen = curses.initscr()
    main_menu = Menu(screen)
    main_menu.display_main_menu()
    curses.wrapper(run_pyarcade())


if __name__ == '__main__':
    curses.wrapper(run_pyarcade())

