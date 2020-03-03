from pyarcade.toy_ui import *
from curses import wrapper


def run_pyarcade():
    """ This will effectively become our program entrypoint.
    """
    wrapper(UserInterface)

