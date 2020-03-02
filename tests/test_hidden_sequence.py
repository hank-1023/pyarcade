import unittest
from pyarcade.mastermind.hidden_sequence_mastermind import *


class HiddenSequenceMastermindTestCase(unittest.TestCase):
    def test_hidden_sequence_init(self):
        game = HiddenSequenceMastermind()
        self.assertEqual(len(game.generate_hidden_sequence()), 4)

    def test_hidden_sequence_execute_input_nowhere(self):
        mastermind = HiddenSequenceMastermind()
        mastermind.current_hidden_sequence = [1, 2, 3, 4]

        mastermind.execute_input([5, 6, 7, 8])
        correct, misplaced, nowhere = mastermind.current_result
        self.assertEqual(correct, [])
        self.assertEqual(misplaced, [])
        self.assertEqual(nowhere, [0, 1, 2, 3])

    def test_hidden_sequence_execute_input_misplaced(self):
        mastermind = HiddenSequenceMastermind()
        mastermind.current_hidden_sequence = [1, 2, 3, 4]

        mastermind.execute_input([2, 3, 1, 4])
        correct, misplaced, nowhere = mastermind.current_result
        self.assertEqual(correct, [3])
        self.assertEqual(misplaced, [0, 1, 2])
        self.assertEqual(nowhere, [])

    def test_hidden_sequence_execute_input_correct(self):
        mastermind = HiddenSequenceMastermind()
        mastermind.current_hidden_sequence = [1, 2, 3, 4]

        mastermind.execute_input([1, 2, 3, 4])
        correct, misplaced, nowhere = mastermind.current_result
        self.assertEqual(correct, [0, 1, 2, 3])
        self.assertEqual(misplaced, [])
        self.assertEqual(nowhere, [])
        self.assertEqual(mastermind.game_state, GameState.WIN)

    def test_hidden_sequence_get_display_string(self):
        mastermind = HiddenSequenceMastermind()
        mastermind.current_hidden_sequence = [1, 2, 3, 4]

        mastermind.execute_input([2, 3, 1, 4])
        desired_string = "Correct digits: [4]\n" \
                         "Misplaced digits: [1, 2, 3]\n" \
                         "Numbers on these digits are not existed: []"
        self.assertEqual(mastermind.get_display_string(), desired_string)

    def test_hidden_sequence_reset(self):
        mastermind = HiddenSequenceMastermind()
        mastermind.current_hidden_sequence = [1, 2, 3, 4]

        mastermind.execute_input([1, 2, 3, 4])
        mastermind.reset()

        self.assertEqual(len(mastermind.current_hidden_sequence), 4)
        self.assertEqual(mastermind.current_result, None)
        self.assertEqual(mastermind.game_state, GameState.PENDING)
        self.assertEqual(mastermind.guess_history, [])
