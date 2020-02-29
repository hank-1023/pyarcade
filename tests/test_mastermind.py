from pyarcade.start import *
import unittest


class MastermindTestCase(unittest.TestCase):

    def test_generate_random_sequence(self):
        game = iMastermind(GameType.HIDDEN_SEQUENCE)
        self.assertEqual(len(game.generate_hidden_sequence()), 4)

    def test_generate_game_matrix(self):
        game = iMastermind(GameType.MINESWEEPER)
        matrix = game.generate_game_matrix()
        self.assertEqual(len(matrix), 4)
        self.assertEqual(len(matrix[0]), 4)

    def test_execute_hs_input(self):
        game = iMastermind(GameType.HIDDEN_SEQUENCE)
        game.current_hidden_sequence = [1, 2, 3, 4]

        correct, misplaced, nowhere = game.execute_hs_input([5, 6, 7, 8])
        self.assertEqual(correct, [])
        self.assertEqual(misplaced, [])
        self.assertEqual(nowhere, [0, 1, 2, 3])

        correct, misplaced, nowhere = game.execute_hs_input([2, 3, 1, 4])
        self.assertEqual(correct, [3])
        self.assertEqual(misplaced, [0, 1, 2])
        self.assertEqual(nowhere, [])

        correct, misplaced, nowhere = game.execute_hs_input([2, 3, 0, 4])
        self.assertEqual(correct, [3])
        self.assertEqual(misplaced, [0, 1])
        self.assertEqual(nowhere, [2])

    def test_execute_sweeper_input(self):
        game = iMastermind(GameType.MINESWEEPER)
        game.game_matrix = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 1]]

        result = game.execute_sweeper_input([0, 0])
        self.assertEqual(result, 1)

        result = game.execute_sweeper_input([0, 0])
        self.assertEqual(result, -1)

        result = game.execute_sweeper_input([1, 2])
        self.assertEqual(result, 0)

    def test_reset_sweeper(self):
        game = iMastermind(GameType.MINESWEEPER)

        # Test reset when there hasn't been user inputs
        game.reset()
        matrix = game.game_matrix
        self.assertEqual(len(matrix), 4)
        self.assertEqual(len(matrix[0]), 4)
        self.assertEqual(game.remain_count, 14)
        self.assertEqual(game.guess_history, [])

        # Test reset during game
        game.execute_sweeper_input([0, 0])
        game.execute_sweeper_input([1, 1])
        game.execute_sweeper_input([2, 3])
        game.reset()
        self.assertEqual(len(matrix), 4)
        self.assertEqual(len(matrix[0]), 4)
        self.assertEqual(game.remain_count, 14)
        self.assertEqual(game.guess_history, [])

    def test_start(self):
        run_pyarcade(GameType.HIDDEN_SEQUENCE)
        run_pyarcade(GameType.MINESWEEPER)
