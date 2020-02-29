from pyarcade.mastermind.hidden_sequence_mastermind import *
from pyarcade.mastermind.mine_sweeper_mastermind import *
from pyarcade.mastermind.war_mastermind import *


class iMastermindFactory:
    def create_master_mind(self, game_size: int, game_range: int) -> iMastermind:
        raise NotImplementedError


class HiddenSequenceMastermindFactory(iMastermindFactory):
    def create_master_mind(self, game_size: int, game_range: int) -> HiddenSequenceMastermind:
        return HiddenSequenceMastermind(game_size, game_range)


class MineSweeperMastermindFactory(iMastermindFactory):
    def create_master_mind(self, game_size: int, game_range: int) -> MineSweeperMastermind:
        return MineSweeperMastermind(game_size, game_range)


class WarGameMastermindFactory(iMastermindFactory):
    def create_master_mind(self, game_size: int, game_range: int) -> iMastermind:
        return WarMastermind()
