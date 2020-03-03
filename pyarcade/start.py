import curses
from pyarcade.ui import Menu


def run_pyarcade():
    """ This will effectively become our program entrypoint.
    """
    screen = curses.initscr()
    main_menu = Menu(screen)
    main_menu.display_main_menu()
    curses.wrapper(run_pyarcade())
