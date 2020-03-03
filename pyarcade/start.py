from pyarcade.toy_ui import *


def run_pyarcade():
    """ This will effectively become our program entrypoint.
    """
    curses.wrapper(UserInterface)


if __name__ == '__main__':
    run_pyarcade()
