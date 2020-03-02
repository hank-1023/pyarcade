import unittest
from pyarcade import ui


class UITestCase(unittest.TestCase):
    """
    Feature tests for the User Interface
    """

    def test_ui_war(self):
        wargame = (ui.MyApp)
        wargame.curses.KEY_DOWN
        wargame.curses.KEY_ENTER
        wargame.curses.KEY_DOWN
        wargame.curses.KEY_ENTER

