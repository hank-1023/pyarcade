from pyarcade.mastermind.hidden_sequence_mastermind import *
from pyarcade.mastermind.mine_sweeper_mastermind import *
from pyarcade.mastermind.war_mastermind import *


class iMastermindCreator:
    def __init__(self):
        self.mastermind = self.create_mastermind()

    # The factory method
    def create_mastermind(self) -> iMastermind:
        raise NotImplementedError

    def execute_input(self, game_input: [int]):
        self.mastermind.execute_input(game_input)

    def reset(self):
        self.mastermind.reset()

    def get_display_string(self) -> str:
        return self.mastermind.get_display_string()

    def get_game_state(self) -> GameState:
        return self.mastermind.game_state

    def get_guess_history(self):
        return self.mastermind.guess_history


class HiddenSequenceMastermindCreator(iMastermindCreator):
    def create_mastermind(self) -> HiddenSequenceMastermind:
        return HiddenSequenceMastermind()


class MineSweeperMastermindCreator(iMastermindCreator):
    def create_mastermind(self) -> MineSweeperMastermind:
        return MineSweeperMastermind()


class WarGameMastermindCreator(iMastermindCreator):
    def create_mastermind(self) -> iMastermind:
        return WarMastermind()
