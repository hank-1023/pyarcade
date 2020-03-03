from pyarcade.ui import *
from curses import wrapper


def run_pyarcade():
    """ This will effectively become our program entrypoint.
    """
    wrapper(UserInterface)


if __name__ == '__main__':
    run_pyarcade()
