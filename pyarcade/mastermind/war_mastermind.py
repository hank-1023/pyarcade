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

        if self.player_cards and self.dealer_cards:
            player_card = self.player_cards.pop()
            dealer_card = self.dealer_cards.pop()
            if player_card.value == dealer_card.value:
                while player_card.value == dealer_card.value:
                    self.standby.append(player_card)
                    self.standby.append(dealer_card)
                    if len(self.player_cards) == 0:
                        print("Player Lost!")
                        self.standby.clear()
                        self.update_ui()
                        return False
                    self.standby.append(self.player_cards.pop())
                    if len(self.dealer_cards) == 0:
                        print("Player Win!")
                        self.standby.clear()
                        self.update_ui()
                        return False
                    self.standby.append(self.dealer_cards.pop())
                    if len(self.player_cards) == 0:
                        print("Player Lost!")
                        self.standby.clear()
                        self.update_ui()
                        return False
                    player_card = self.player_cards.pop()
                    if len(self.dealer_cards) == 0:
                        print("Player Win!")
                        self.standby.clear()
                        self.update_ui()
                        return False
                    dealer_card = self.dealer_cards.pop()

            if player_card.value > dealer_card.value:
                self.standby.append(player_card)
                self.standby.append(dealer_card)
                self.player_faceup.extend(self.standby)
                print("Player get the cards:" + str(len(self.standby)))
                self.standby.clear()
                self.update_ui()
                return True
            else:
                self.standby.append(player_card)
                self.standby.append(dealer_card)
                self.dealer_faceup.extend(self.standby)
                print("Dealer get the cards:" + str(len(self.standby)))
                self.standby.clear()
                self.update_ui()
                return True

        elif len(self.player_cards) == 0:
            if len(self.player_faceup) == 0:
                print("Player Lost !")
                return False
            random.shuffle(self.player_faceup)
            self.player_cards.extend(self.player_faceup)
            self.player_faceup.clear()
            self.play_war("go")
            self.update_ui(self)
            return True

        elif len(self.dealer_cards) == 0:
            if len(self.dealer_faceup) == 0:
                print("Player Win !")
                self.update_ui(self)
                return False
            random.shuffle(self.dealer_faceup)
            self.dealer_cards.extend(self.dealer_faceup)
            self.dealer_faceup.clear()
            self.play_war("go")
            self.update_ui()
            return True

    def check_win(self):
        """
        Called by on_user_input after execute_input() to check if user has won the game
        """
        raise NotImplementedError

    def update_ui(self):
        raise NotImplementedError

    def reset(self):
        self.player_cards = []
        self.dealer_cards = []
        self.player_faceup = []
        self.dealer_faceup = []
        self.standby = []
