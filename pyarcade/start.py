import os

from pyarcade.toy_ui import *


def run_pyarcade():
    """ This will effectively become our program entrypoint.
    """
    environ_variables = {"TERM": "linux", "TERMINFO": "/etc/terminfo"}
    os.environ.update(environ_variables)
    curses.wrapper(UserInterface)
