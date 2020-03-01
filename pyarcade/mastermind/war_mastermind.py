from random import random
from pyarcade.mastermind.mastermind import *

CARD_SUITE = ["H", "D", "S", "C"]
RANK_SEQUENCE = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card:
    def __init__(self, suite, rank):
        self.suite, self.rank = suite, rank

    def __eq__(self, other):
        return RANK_SEQUENCE.index(self.rank) == RANK_SEQUENCE.index(other.rank)

    def __gt__(self, other):
        return RANK_SEQUENCE.index(self.rank) > RANK_SEQUENCE.index(other.rank)

    def __lt__(self, other):
        return RANK_SEQUENCE.index(self.rank) < RANK_SEQUENCE.index(other.rank)


class WarMastermind(iMastermind):
    def __init__(self):
        super().__init__()
        # for the card arrays, index 0 are considered top of deck
        self.player_cards = []
        self.dealer_cards = []
        self.card_pool = []
        self.player_win = False
        self.dealer_win = False

        self.prepare_cards()

    def prepare_cards(self):
        """
        This is the method we use to give cards to player and dealer
        :return: cards for player, cards for dealer
        """
        cards = [Card(s, r) for s in CARD_SUITE for r in RANK_SEQUENCE]
        random.shuffle(cards)
        self.player_cards = cards
        random.shuffle(cards)
        self.dealer_cards = cards

    def execute_input(self, game_input: [int]):
        player_card = self.player_cards.pop(0)
        dealer_card = self.dealer_cards.pop(0)
        self.card_pool = [player_card, dealer_card]

        if player_card == dealer_card:
            self.war()
        elif player_card > dealer_card:
            self.player_cards.extend(self.card_pool)
            self.card_pool = []
            self.check_win()
        elif dealer_card > player_card:
            self.dealer_cards.extend(self.card_pool)
            self.card_pool = []
            self.check_win()

    def war(self):
        self.check_win()
        if self.dealer_win or self.player_win:
            return

        self.card_pool.append(self.player_cards.pop(0))  # The player's face down card
        self.card_pool.append(self.dealer_cards.pop(0))  # Dealer's face down card

        player_face_up = self.player_cards.pop(0)
        dealer_face_up = self.dealer_cards.pop(0)

        self.card_pool.append(player_face_up)
        self.card_pool.append(dealer_face_up)

        if player_face_up == dealer_face_up:
            self.war()
        elif player_face_up > dealer_face_up:
            self.player_cards.extend(self.card_pool)
            self.card_pool = []
        elif dealer_face_up > player_face_up:
            self.dealer_cards.extend(self.card_pool)
            self.card_pool = []

    def check_win(self):
        """
        Called by on_user_input after execute_input() to check if user has won the game
        """
        if 2 > len(self.player_cards) != len(self.dealer_cards):
            self.dealer_win = True
        elif 2 > len(self.dealer_cards) != len(self.player_cards):
            self.player_win = True
        elif len(self.dealer_cards) == len(self.player_cards) == 0:
            # If cards runs out during war, the player ties with dealer
            self.dealer_win = True
            self.player_win = True

    def update_ui(self):
        raise NotImplementedError

    def reset(self):
        self.prepare_cards()
        self.card_pool = []
        self.player_win = False
        self.dealer_win = False
