import unittest
from pyarcade.mine_sweeper_mastermind import *
from pyarcade.imastermind import *


class MineSweeperMastermindTestCase(unittest.TestCase):
    def test_mine_sweeper_init(self):
        mastermind = MineSweeperMastermind()
        self.assertEqual(len(mastermind.display_board), 4)
        self.assertEqual(len(mastermind.display_board[0]), 4)
        self.assertEqual(len(mastermind.game_matrix), 6)
        self.assertEqual(len(mastermind.game_matrix[0]), 6)

    def test_mine_sweeper_execute_input_normal(self):
        mastermind = MineSweeperMastermind()
        mastermind.game_matrix = [[0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 1, 1, 0],
                                  [0, 0, 1, 2, -1, 0],
                                  [0, 0, 1, -1, 2, 0],
                                  [0, 0, 1, 1, 1, 0],
                                  [0, 0, 0, 0, 0, 0]]
        mastermind.execute_input([0, 2])
        self.assertEqual(mastermind.display_board[0][2], "1")
        self.assertEqual(mastermind.game_state, GameState.PENDING)

    def test_mine_sweeper_input_lose(self):
        mastermind = MineSweeperMastermind()
        mastermind.game_matrix = [[0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 1, 1, 0],
                                  [0, 0, 1, 2, -1, 0],
                                  [0, 0, 1, -1, 2, 0],
                                  [0, 0, 1, 1, 1, 0],
                                  [0, 0, 0, 0, 0, 0]]
        mastermind.execute_input([1, 3])
        self.assertEqual(mastermind.game_state, GameState.LOSE)

    def test_mine_sweeper_win(self):
        mastermind = MineSweeperMastermind()
        mastermind.game_matrix = [[0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 1, 1, 0],
                                  [0, 0, 1, 2, -1, 0],
                                  [0, 0, 1, -1, 2, 0],
                                  [0, 0, 1, 1, 1, 0],
                                  [0, 0, 0, 0, 0, 0]]
        # The execute_input's index should still relate to the actual board's index
        mastermind.execute_input([0, 0])
        mastermind.execute_input([0, 1])
        mastermind.execute_input([0, 2])
        mastermind.execute_input([0, 3])
        mastermind.execute_input([1, 0])
        mastermind.execute_input([1, 1])
        mastermind.execute_input([1, 2])
        mastermind.execute_input([2, 0])
        mastermind.execute_input([2, 1])
        mastermind.execute_input([2, 3])
        mastermind.execute_input([3, 0])
        mastermind.execute_input([3, 1])
        mastermind.execute_input([3, 2])
        mastermind.execute_input([3, 3])

        self.assertEqual(mastermind.game_state, GameState.WIN)

    def test_mine_sweeper_get_display_string(self):
        mastermind = MineSweeperMastermind()
        mastermind.game_matrix = [[0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 1, 1, 0],
                                  [0, 0, 1, 2, -1, 0],
                                  [0, 0, 1, -1, 2, 0],
                                  [0, 0, 1, 1, 1, 0],
                                  [0, 0, 0, 0, 0, 0]]
        mastermind.execute_input([0, 2])
        desired_str = "['x', 'x', '1', 'x']\n" \
                      "['x', 'x', 'x', 'x']\n" \
                      "['x', 'x', 'x', 'x']\n" \
                      "['x', 'x', 'x', 'x']\n"

        self.assertEqual(desired_str, mastermind.get_display_string())

    def test_mine_sweeper_reset(self):
        mastermind = MineSweeperMastermind()
        mastermind.execute_input([1, 3])
        mastermind.reset()

        x_count = sum(sublist.count("x") for sublist in mastermind.display_board)
        self.assertEqual(x_count, 16)
        self.assertEqual(len(mastermind.game_matrix), 6)
        self.assertEqual(len(mastermind.game_matrix[0]), 6)
        self.assertEqual(mastermind.guess_history, [])
        self.assertEqual(mastermind.game_state, GameState.PENDING)
