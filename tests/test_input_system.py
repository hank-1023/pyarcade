import unittest
from pyarcade.input_system import *
import os


class TestInputSystem(unittest.TestCase):

    def test_parse_input(self):
        input_manager = InputManager()
        self.assertEqual(input_manager.parse_input("reset"), (0, []))
        self.assertEqual(input_manager.parse_input("clear"), (1, []))
        self.assertEqual(input_manager.parse_input("123"), (-1, []))
        self.assertEqual(input_manager.parse_input("1234"), (2, [1, 2, 3, 4]))
        self.assertEqual(input_manager.parse_input("abc"), (-1, []))
        self.assertEqual(input_manager.parse_input("1a23"), (-1, []))

    def test_client(self):
        this_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(this_folder, 'input1234.txt')
        client = Client(file_path)
        client.master_mind.current_hidden_sequence = [1, 2, 3, 4]
        self.assertTrue(client.start())

        file_path = os.path.join(this_folder, 'inputEmpty.txt')
        client = Client(file_path)
        self.assertFalse(client.start())

        file_path = os.path.join(this_folder, 'inputVarious.txt')
        client = Client(file_path)
        client.master_mind.current_hidden_sequence = [1, 2, 3, 4]
        self.assertTrue(client.start())

        file_path = os.path.join(this_folder, 'inputWithClear.txt')
        client = Client(file_path)
        client.master_mind.current_hidden_sequence = [1, 2, 3, 4]
        self.assertTrue(client.start())


if __name__ == '__main__':
    unittest.main()
