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

    def test_client_clear_all_history(self):
        client = Client()
        client.start_game(GameType.HIDDEN_SEQUENCE)

        # Suppose the generated hidden sequence is now [1, 2, 3, 4]
        client.mastermind_creator.mastermind.current_hidden_sequence = [1, 2, 3, 4]
        client.parse_execute_input("1234")
        client.parse_execute_input("clear")

        self.assertEqual(client.get_all_history(), {"Win": 0, "Lose": 0})


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

        self.assertEqual(client.get_mastermind_local_history(), [[0, 0]])

    def test_client_minesweeper_normal_input(self):
        client = Client()
        client.start_game(GameType.MINE_SWEEPER)

        assumed_game_matrix = [[0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0],
                               [0, 1, 1, 1, 0, 0],
                               [0, 2, -1, 1, 0, 0],
                               [0, -1, 2, 1, 0, 0],
                               [0, 0, 0, 0, 0, 0]]

        client.mastermind_creator.mastermind.game_matrix = assumed_game_matrix

        client.parse_execute_input("0, 0")
        client.parse_execute_input("1, 1")

        desired_output = "['0', 'x', 'x', 'x']\n" \
                         "['x', '1', 'x', 'x']\n" \
                         "['x', 'x', 'x', 'x']\n" \
                         "['x', 'x', 'x', 'x']\n"

        self.assertEqual(client.get_display_data(), desired_output)

    def test_mine_sweeper_multiple_get_display(self):
        client = Client()
        client.start_game(GameType.MINE_SWEEPER)

        assumed_game_matrix = [[0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0],
                               [0, 1, 1, 1, 0, 0],
                               [0, 2, -1, 1, 0, 0],
                               [0, -1, 2, 1, 0, 0],
                               [0, 0, 0, 0, 0, 0]]

        client.mastermind_creator.mastermind.game_matrix = assumed_game_matrix

        client.parse_execute_input("0, 0")
        client.parse_execute_input("1, 1")

        desired_output = "['0', 'x', 'x', 'x']\n" \
                         "['x', '1', 'x', 'x']\n" \
                         "['x', 'x', 'x', 'x']\n" \
                         "['x', 'x', 'x', 'x']\n"
        self.assertEqual(client.get_display_data(), desired_output)

        client.parse_execute_input("1, 2")

        desired_output = "['0', 'x', 'x', 'x']\n" \
                         "['x', '1', '1', 'x']\n" \
                         "['x', 'x', 'x', 'x']\n" \
                         "['x', 'x', 'x', 'x']\n"
        self.assertEqual(client.get_display_data(), desired_output)

    def test_client_step_on_bomb(self):
        client = Client()
        client.start_game(GameType.MINE_SWEEPER)

        assumed_game_matrix = [[0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0],
                               [0, 1, 1, 1, 0, 0],
                               [0, 2, -1, 1, 0, 0],
                               [0, -1, 2, 1, 0, 0],
                               [0, 0, 0, 0, 0, 0]]

        client.mastermind_creator.mastermind.game_matrix = assumed_game_matrix

        client.parse_execute_input("0, 0")
        client.parse_execute_input("1, 1")
        client.parse_execute_input("2, 1")

        desired_output = "['0', 'x', 'x', 'x']\n" \
                         "['x', '1', 'x', 'x']\n" \
                         "['x', '*', 'x', 'x']\n" \
                         "['x', 'x', 'x', 'x']\n"

        self.assertEqual(client.get_display_data(), desired_output)
        self.assertEqual(client.get_game_state(), GameState.LOSE)
        self.assertEqual(client.get_all_history(), {"Win": 0, "Lose": 1})

    def test_client_minesweeper_reset(self):
        client = Client()
        client.start_game(GameType.MINE_SWEEPER)

        client.parse_execute_input("0, 0")
        client.parse_execute_input("1, 1")
        client.parse_execute_input("2, 1")

        client.parse_execute_input("reset")
        desired_output = "['x', 'x', 'x', 'x']\n" \
                         "['x', 'x', 'x', 'x']\n" \
                         "['x', 'x', 'x', 'x']\n" \
                         "['x', 'x', 'x', 'x']\n"

        self.assertEqual(client.get_display_data(), desired_output)
        self.assertEqual(client.get_game_state(), GameState.PENDING)
        self.assertEqual(client.get_mastermind_local_history(), [])

    def test_client_restart_different_game(self):
        client = Client()
        # First start a hidden sequence game
        client.start_game(GameType.HIDDEN_SEQUENCE)

        client.mastermind_creator.mastermind.current_hidden_sequence = [1, 2, 3, 4]

        client.parse_execute_input("2341")
        client.parse_execute_input("1234")

        self.assertEqual(client.get_game_state(), GameState.WIN)

        client.start_game(GameType.MINE_SWEEPER)
        self.assertEqual(client.get_game_state(), GameState.PENDING)

        assumed_game_matrix = [[0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0],
                               [0, 1, 1, 1, 0, 0],
                               [0, 2, -1, 1, 0, 0],
                               [0, -1, 2, 1, 0, 0],
                               [0, 0, 0, 0, 0, 0]]

        client.mastermind_creator.mastermind.game_matrix = assumed_game_matrix

        client.parse_execute_input("0, 0")
        client.parse_execute_input("1, 1")
        client.parse_execute_input("2, 1")

        desired_output = "['0', 'x', 'x', 'x']\n" \
                         "['x', '1', 'x', 'x']\n" \
                         "['x', '*', 'x', 'x']\n" \
                         "['x', 'x', 'x', 'x']\n"

        self.assertEqual(client.get_display_data(), desired_output)
        self.assertEqual(client.get_game_state(), GameState.LOSE)

    def test_client_war_invalid(self):
        client = Client()
        client.start_game(GameType.WAR)

        client.parse_execute_input("jfdaj")
        client.parse_execute_input("123")
        client.parse_execute_input("1, 2\n")

        self.assertEqual(client.get_mastermind_local_history(), [])
        self.assertEqual(client.get_game_state(), GameState.PENDING)

    def test_client_war_player_advantage(self):
        client = Client()
        client.start_game(GameType.WAR)
        player_rank_sequence = ["J", "Q", "K", "A"]
        dealer_rank_sequence = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]

        client.mastermind_creator.mastermind.dealer_deck = \
            [Card(s, r) for s in range(4) for r in dealer_rank_sequence]
        client.mastermind_creator.mastermind.player_deck = \
            [Card(s, r) for s in range(9) for r in player_rank_sequence]

        desired_output = "Player deck: [(0, 'J'), (0, 'Q'), (0, 'K'), (0, 'A'), (1, 'J')] ...\n" \
                         "Dealer deck: [(0, '2'), (0, '3'), (0, '4'), (0, '5'), (0, '6')] ...\n"
        self.assertEqual(client.get_display_data(), desired_output)

        while client.get_game_state() != GameState.WIN:
            client.parse_execute_input("deal")

        desired_output = "Player deck: [(8, 'A'), (0, 'J'), (0, '2'), (0, 'Q'), (0, '3')] ...\n" \
                         "Dealer deck: [(3, '10')]\n"
        self.assertEqual(client.get_display_data(), desired_output)
        self.assertEqual(client.get_game_state(), GameState.WIN)


