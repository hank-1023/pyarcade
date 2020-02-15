from pyarcade.input_system import *
from pyarcade.start import *
import os
import unittest


class MastermindTestCase(unittest.TestCase):
    def test_generate_random_sequence(self):
        game = Mastermind()
        self.assertEqual(len(game.generate_hidden_sequence()), 4)

    def test_clear_during_game(self):
        this_folder = os.path.dirname(os.path.abspath(__file__))

        file_path = os.path.join(this_folder, 'inputVarious.txt')
        client = Client(file_path)
        client.start()

        client.master_mind.clear_history()
        self.assertEqual(client.master_mind.guess_history, [])

    def test_reset_during_game(self):
        this_folder = os.path.dirname(os.path.abspath(__file__))

        file_path = os.path.join(this_folder, 'inputVarious.txt')
        client = Client(file_path)
        previous_sequence = client.master_mind.current_hidden_sequence
        client.start()
        client.master_mind.reset()
        current_sequence = client.master_mind.current_hidden_sequence

        self.assertNotEqual(previous_sequence, current_sequence)
        self.assertEqual(client.master_mind.guess_history, [])

    def test_start(self):
        os.system("python start.py")
