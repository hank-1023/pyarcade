import unittest
from pyarcade.imastermind import *


class HiddenSequenceMastermindTestCase(unittest.TestCase):
    def test_imastermind_implementation_init(self):
        imastermind = iMastermind()
        self.assertEqual(imastermind.game_state, GameState.PENDING)
        self.assertEqual(imastermind.guess_history, [])

    def test_imastermind_direct_call(self):
        imastermind = iMastermind()

        with self.assertRaises(NotImplementedError):
            imastermind.execute_input([])
        with self.assertRaises(NotImplementedError):
            imastermind.check_win()
        with self.assertRaises(NotImplementedError):
            imastermind.get_display_string()
        with self.assertRaises(NotImplementedError):
            imastermind.reset()
