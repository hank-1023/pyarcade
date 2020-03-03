import os

from pyarcade.toy_ui import *


def run_pyarcade():
    """ This will effectively become our program entrypoint.
    """
    curses.wrapper(UserInterface)
