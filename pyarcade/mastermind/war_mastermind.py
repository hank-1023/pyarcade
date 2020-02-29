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


class WarMastermind(Mastermind):
    def __init__(self):
        super().__init__()
        self.player_cards = []
        self.dealer_cards = []
        self.player_faceup = []
        self.dealer_faceup = []
        self.standby = []

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
        player_card = self.player_cards.pop()
        dealer_card = self.dealer_cards.pop()

        if player_card == dealer_card:
            return


    def reset(self):
        self.player_cards = []
        self.dealer_cards = []
        self.player_faceup = []
        self.dealer_faceup = []
        self.standby = []
