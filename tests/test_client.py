import unittest
from pyarcade.client import *


class ClientTestCase(unittest.TestCase):
    """
    Feature tests for the program
    """

    def test_client_mine_sweeper(self):
        client = Client(GameType.MINE_SWEEPER)
        client.parse_execute_input("0, 0")
        client.parse_execute_input("1, 2")
        display_string = client.get_display_data()
        print(display_string)
