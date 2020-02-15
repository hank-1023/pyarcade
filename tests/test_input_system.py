import unittest
from pyarcade.input_system import *


class TestInputSystem(unittest.TestCase):

    def test_parse_input(self):
        input_manager = InputManager()
        self.assertEqual(input_manager.parse_input("reset"), (0, []))
        self.assertEqual(input_manager.parse_input("clear"), (1, []))
        self.assertEqual(input_manager.parse_input("123"), (2, [1, 2, 3]))
        self.assertEqual(input_manager.parse_input("abc"), (-1, []))
        self.assertEqual(input_manager.parse_input("1a23"), (-1, []))

    def test_client(self):
        client = Client("pyarcade/input1234.txt")
        client.start()


if __name__ == '__main__':
    unittest.main()
