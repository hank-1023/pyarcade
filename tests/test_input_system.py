import unittest
from pyarcade.input_system import *
from pyarcade.mastermind import *


class TestInputSystem(unittest.TestCase):

    def test_game_input_hidden_sequence(self):
        """
        Module test for hidden sequence game
        """
        input_manager = InputManager(GameType.HIDDEN_SEQUENCE)
        self.assertEqual(input_manager.mastermind.game_state, GameState.PENDING)
        # Suppose the hidden sequence is now [1, 2, 3, 4]
        input_manager.mastermind.current_hidden_sequence = [1, 2, 3, 4]

        input_manager.parse_input("123")
        input_manager.parse_input("12a3")
        input_manager.parse_input("12345")
        input_manager.parse_input("hehe")
        input_manager.parse_input("")
        # Test if all above inputs are ignored by mastermind
        self.assertEqual(len(input_manager.mastermind.guess_history), 0)

        input_manager.parse_input("2341")
        input_manager.parse_input("8765")
        self.assertEqual(len(input_manager.mastermind.guess_history), 2)

        input_manager.parse_input("clear")
        self.assertEqual(len(input_manager.mastermind.guess_history), 0)

        input_manager.parse_input("1234")
        self.assertEqual(input_manager.mastermind.game_state, GameState.WIN)

        input_manager.parse_input("reset")
        self.assertEqual(len(input_manager.mastermind.guess_history), 0)
        self.assertEqual(len(input_manager.mastermind.current_hidden_sequence), 4)
        self.assertEqual(input_manager.mastermind.game_state, GameState.PENDING)

    def test_game_input_mine_sweeper(self):
        """
        Module test for mine sweeper game
        """
        input_manager = InputManager(GameType.MINESWEEPER)
        mastermind = input_manager.mastermind

        self.assertEqual(mastermind.game_state, GameState.PENDING)

        self.assertEqual(len(mastermind.game_matrix), 4)
        self.assertEqual(len(mastermind.game_matrix[0]), 4)
        # Checking if there are two bombs
        self.assertEqual(sum([i.count(1) for i in mastermind.game_matrix]), 2)
        self.assertEqual(mastermind.remain_count, 14)

        # Now change the game_matrix for easy testing
        mastermind.game_matrix = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
        input_manager.parse_input("1, 1, 1")
        input_manager.parse_input("ab")
        input_manager.parse_input("1ab2")
        input_manager.parse_input("")
        input_manager.parse_input("-1, -1")
        input_manager.parse_input("100, 100")
        self.assertEqual(len(mastermind.guess_history), 0)

        # Test repeated input
        input_manager.parse_input("0, 0")
        input_manager.parse_input("0,  0")
        self.assertEqual(mastermind.remain_count, 13)

        input_manager.parse_input("2, 3")
        input_manager.parse_input("1, 2")
        self.assertEqual(len(mastermind.guess_history), 3)
        self.assertEqual(mastermind.remain_count, 12)
        self.assertEqual(mastermind.game_state, GameState.LOSE)

        input_manager.parse_input("reset")
        self.assertEqual(mastermind.game_state, GameState.PENDING)
        self.assertEqual(mastermind.remain_count, 14)
        self.assertEqual(len(mastermind.game_matrix), 4)
        self.assertEqual(len(mastermind.game_matrix[0]), 4)

    def test_minesweeper_success(self):
        input_manager = InputManager(GameType.MINESWEEPER)
        mastermind = input_manager.mastermind

        mastermind.game_matrix = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
        input_manager.parse_input("0, 0")
        input_manager.parse_input("0, 1")
        input_manager.parse_input("0, 2")
        input_manager.parse_input("0, 3")
        input_manager.parse_input("1, 0")
        input_manager.parse_input("1, 1")
        input_manager.parse_input("1, 3")
        input_manager.parse_input("2, 0")
        input_manager.parse_input("2, 1")
        input_manager.parse_input("2, 2")
        input_manager.parse_input("2, 3")
        input_manager.parse_input("3, 0")
        input_manager.parse_input("3, 1")
        input_manager.parse_input("3, 2")

        self.assertEqual(mastermind.game_state, GameState.WIN)


if __name__ == '__main__':
    unittest.main()
