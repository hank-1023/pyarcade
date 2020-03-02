import unittest
from pyarcade.client import *


class ClientTestCase(unittest.TestCase):
    """
    Feature tests for the program
    """

    def test_client_hidden_sequence_invalid(self):
        client = Client()
        client.start_game(GameType.HIDDEN_SEQUENCE)

        # Suppose the generated hidden sequence is now [1, 2, 3, 4]
        client.mastermind_creator.mastermind.current_hidden_sequence = [1, 2, 3, 4]

        client.parse_execute_input("123")
        client.parse_execute_input("12a3")
        client.parse_execute_input("12345")
        client.parse_execute_input("hehe")
        client.parse_execute_input("")
        # Test if all above inputs are ignored by mastermind
        self.assertEqual(len(client.get_mastermind_local_history()), 0)

    def test_client_hidden_sequence_valid_input(self):
        client = Client()
        client.start_game(GameType.HIDDEN_SEQUENCE)

        # Suppose the generated hidden sequence is now [1, 2, 3, 4]
        client.mastermind_creator.mastermind.current_hidden_sequence = [1, 2, 3, 4]

        client.parse_execute_input("2341")
        client.parse_execute_input("8765")
        self.assertEqual(client.get_mastermind_local_history(), [[2, 3, 4, 1], [8, 7, 6, 5]])
        self.assertEqual(client.get_game_state(), GameState.PENDING)

    def test_client_hidden_sequence_win(self):
        client = Client()
        client.start_game(GameType.HIDDEN_SEQUENCE)

        # Suppose the generated hidden sequence is now [1, 2, 3, 4]
        client.mastermind_creator.mastermind.current_hidden_sequence = [1, 2, 3, 4]
        client.parse_execute_input("1234")

        self.assertEqual(client.get_all_history(), {"Win": 1, "Lose": 0})
        self.assertEqual(client.get_game_state(), GameState.WIN)

    def test_client_hidden_sequence_reset(self):
        client = Client()
        client.start_game(GameType.HIDDEN_SEQUENCE)

        # Suppose the generated hidden sequence is now [1, 2, 3, 4]
        client.mastermind_creator.mastermind.current_hidden_sequence = [1, 2, 3, 4]

        client.parse_execute_input("2341")
        client.parse_execute_input("8765")
        client.parse_execute_input("reset")

        self.assertEqual(len(client.get_mastermind_local_history()), 0)
        self.assertEqual(client.get_game_state(), GameState.PENDING)

        # See if history has been reset
        client.parse_execute_input("8427")
        self.assertEqual(client.get_mastermind_local_history(), [[8, 4, 2, 7]])

    def test_client_minesweeper_invalid(self):
        client = Client()
        client.start_game(GameType.MINE_SWEEPER)

        # assumed_game_matrix = [[0, 0, 0, 0, 0, 0],
        #                        [0, 0, 0, 0, 0, 0],
        #                        [0, 1, 1, 1, 0, 0],
        #                        [0, 2, -1, 1, 0, 0],
        #                        [0, -1, 2, 1, 0, 0],
        #                        [0, 0, 0, 0, 0, 0]]
        #
        # client.mastermind_creator.mastermind.game_matrix = assumed_game_matrix

        client.parse_execute_input("1, 1, 1")
        client.parse_execute_input("ab")
        client.parse_execute_input("1ab2")
        client.parse_execute_input("")
        client.parse_execute_input("-1, -1")
        client.parse_execute_input("100, 100")

        self.assertEqual(len(client.get_mastermind_local_history()), 0)
        desired_display = "['x', 'x', 'x', 'x']\n" \
                          "['x', 'x', 'x', 'x']\n" \
                          "['x', 'x', 'x', 'x']\n" \
                          "['x', 'x', 'x', 'x']\n"
        self.assertEqual(desired_display, client.get_display_data())

    def test_client_minesweeper_repeated_input(self):
        client = Client()
        client.start_game(GameType.MINE_SWEEPER)

        client.parse_execute_input("0, 0")
        client.parse_execute_input("0,  0")





