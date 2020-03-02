import random

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
        self.player_deck = []
        self.dealer_deck = []
        self.card_pool = []
        self.player_win = False
        self.dealer_win = False

        self.prepare_cards()

    def prepare_cards(self):
        """
        This is the method we use to give cards to player and dealer
        :return: cards for player, cards for dealer
        """
        self.player_deck = [Card(s, r) for s in CARD_SUITE for r in RANK_SEQUENCE]
        random.shuffle(self.player_deck)
        self.dealer_deck = [Card(s, r) for s in CARD_SUITE for r in RANK_SEQUENCE]
        random.shuffle(self.dealer_deck)

    def execute_input(self, game_input: [int]):
        player_card = self.player_deck.pop(0)
        dealer_card = self.dealer_deck.pop(0)
        self.card_pool = [player_card, dealer_card]

        if player_card == dealer_card:
            self.war()
            self.card_pool = []
            self.check_win()
        elif player_card > dealer_card:
            self.player_deck.extend(self.card_pool)
            self.card_pool = []
            self.check_win()
        elif dealer_card > player_card:
            self.dealer_deck.extend(self.card_pool)
            self.card_pool = []
            self.check_win()

    def war(self):
        self.check_win()
        if self.dealer_win or self.player_win:
            return

        self.card_pool.append(self.player_deck.pop(0))  # The player's face down card
        self.card_pool.append(self.dealer_deck.pop(0))  # Dealer's face down card

        player_face_up = self.player_deck.pop(0)
        dealer_face_up = self.dealer_deck.pop(0)

        self.card_pool.append(player_face_up)
        self.card_pool.append(dealer_face_up)

        if player_face_up == dealer_face_up:
            self.war()
        elif player_face_up > dealer_face_up:
            self.player_deck.extend(self.card_pool)
        elif dealer_face_up > player_face_up:
            self.dealer_deck.extend(self.card_pool)

    def check_win(self):
        """
        Called by on_user_input after execute_input() to check if user has won the game
        """
        if 2 > len(self.player_deck) != len(self.dealer_deck):
            self.dealer_win = True
        elif 2 > len(self.dealer_deck) != len(self.player_deck):
            self.player_win = True
        elif len(self.dealer_deck) == len(self.player_deck) < 2:
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
