from pyarcade.mastermind import Mastermind
import unittest


class MastermindTestCase(unittest.TestCase):
    def test_generate_random_sequence(self):
        game = Mastermind()
        self.assertEqual(len(game.generate_hidden_sequence()), 4)
