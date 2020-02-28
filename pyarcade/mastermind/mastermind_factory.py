from pyarcade.mastermind.hidden_sequence_mastermind import *
from pyarcade.mastermind.mine_sweeper_mastermind import *


class MastermindFactory:
    def create_master_mind(self, game_size: int, game_range: int) -> Mastermind:
        raise NotImplementedError


class HiddenSequenceMastermindFactory(MastermindFactory):
    def create_master_mind(self, game_size: int, game_range: int) -> HiddenSequenceMastermind:
        return HiddenSequenceMastermind(game_size, game_range)


class MineSweeperMastermindFactory(MastermindFactory):
    def create_master_mind(self, game_size: int, game_range: int) -> MineSweeperMastermind:
        return MineSweeperMastermind(game_size, game_range)


class WarGameMastermindFactory(MastermindFactory):
    def create_master_mind(self, game_size: int, game_range: int) -> Mastermind:
        raise NotImplementedError

