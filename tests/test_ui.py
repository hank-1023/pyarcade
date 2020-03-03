import unittest
from pyarcade.ui import Menu
from unittest import mock
from pyarcade import start
import os
import curses

class UITestCase(unittest.TestCase):

    #Feature tests for the User Interface
    os.environ['TERM'] = 'dumb'

    def test_ui_main_menu(self):
        screen = curses.initscr()
        main_menu = Menu(screen)
        main_menu.display_main_menu()
        main_menu.mock.__enter__
