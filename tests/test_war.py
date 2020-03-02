import unittest
from pyarcade.mastermind.war_mastermind import *


class WarMastermindTestCase(unittest.TestCase):
    def test_war_prepare_cards(self):
        mastermind = WarMastermind()
        dealer_deck_length = len(mastermind.dealer_deck)
        player_deck_length = len(mastermind.player_deck)
        self.assertEqual(dealer_deck_length, player_deck_length)

    def test_war_execute_input_same_deck(self):
        mastermind = WarMastermind()
        # Intentionally make the two deck the same
        mastermind.dealer_deck = [Card(s, r) for s in CARD_SUITE for r in RANK_SEQUENCE]
        mastermind.player_deck = [Card(s, r) for s in CARD_SUITE for r in RANK_SEQUENCE]

        while not (mastermind.dealer_win or mastermind.player_win):
            mastermind.execute_input([])

        self.assertTrue(mastermind.dealer_win)
        self.assertTrue(mastermind.player_win)

    def test_war_execute_input_reverse_sorted(self):
        mastermind = WarMastermind()
        mastermind.dealer_deck = [Card(s, r) for s in CARD_SUITE for r in RANK_SEQUENCE]
        mastermind.player_deck = [Card(s, r) for s in CARD_SUITE for r in RANK_SEQUENCE]
        # Make sure the player wins first hand
        mastermind.player_deck.sort(reverse=True)
        mastermind.execute_input([])

        # Since the game might be infinite, only check the array length
        self.assertEqual(51, len(mastermind.dealer_deck))
        self.assertEqual(53, len(mastermind.player_deck))

    def test_war_execute_input_player_advantage(self):
        # Making sure the player wins the game
        player_rank_sequence = ["J", "Q", "K", "A"]
        dealer_rank_sequence = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]

        mastermind = WarMastermind()
        mastermind.dealer_deck = [Card(s, r) for s in range(4) for r in dealer_rank_sequence]
        mastermind.player_deck = [Card(s, r) for s in range(9) for r in player_rank_sequence]

        while not (mastermind.dealer_win or mastermind.player_win):
            mastermind.execute_input([])

        self.assertTrue(mastermind.player_win)
        self.assertFalse(mastermind.dealer_win)

    def test_war_execute_input_dealer_advantage(self):
        # Making sure the dealer wins the game
        dealer_rank_sequence = ["J", "Q", "K", "A"]
        player_rank_sequence = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]

        mastermind = WarMastermind()
        mastermind.dealer_deck = [Card(s, r) for s in range(9) for r in dealer_rank_sequence]
        mastermind.player_deck = [Card(s, r) for s in range(4) for r in player_rank_sequence]

        while not (mastermind.dealer_win or mastermind.player_win):
            mastermind.execute_input([])

        self.assertFalse(mastermind.player_win)
        self.assertTrue(mastermind.dealer_win)

    def test_war_get_display_string(self):
        mastermind = WarMastermind()
        # Intentionally make the two deck the same
        mastermind.dealer_deck = [Card(s, r) for s in CARD_SUITE for r in RANK_SEQUENCE]
        mastermind.player_deck = [Card(s, r) for s in CARD_SUITE for r in RANK_SEQUENCE]

        desired_str = "Player deck: [('H', '2'), ('H', '3'), ('H', '4'), ('H', '5')] ...\n" \
                      "Dealer deck: [('H', '2'), ('H', '3'), ('H', '4'), ('H', '5')] ...\n" \
                      "Card pool: []"

        self.assertEqual(mastermind.get_display_string(), desired_str)

    def test_war_reset(self):
        mastermind = WarMastermind()
        mastermind.execute_input([])

        mastermind.reset()
        self.assertEqual(mastermind.card_pool, [])
        self.assertFalse(mastermind.player_win)
        self.assertFalse(mastermind.dealer_win)
        self.assertEqual(len(mastermind.dealer_deck), 52)
        self.assertEqual(len(mastermind.player_deck), 52)
