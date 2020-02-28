from pyarcade.mastermind.hidden_sequence_mastermind import *
from pyarcade.mastermind.mine_sweeper_mastermind import *


class MastermindFactory:
    def create_master_mind(self) -> Mastermind:
        raise NotImplementedError


class HiddenSequenceMastermindFactory(MastermindFactory):
    def create_master_mind(self) -> HiddenSequenceMastermind:
        return HiddenSequenceMastermind()


class MineSweeperMastermindFactory(MastermindFactory):
    def create_master_mind(self) -> Mastermind:
        return MineSweeperMastermind()


class WarGameMastermindFactory(MastermindFactory):
    def create_master_mind(self) -> Mastermind:
        raise NotImplementedError

