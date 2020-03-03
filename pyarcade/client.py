from typing import Optional

from pyarcade.mastermind_factory import *
from pyarcade.imastermind import *


class GameType(Enum):
    HIDDEN_SEQUENCE = 0
    MINE_SWEEPER = 1
    WAR = 2


class Client:
    def __init__(self):
        self.game_type: Optional[GameType] = None
        self.mastermind_creator: Optional[iMastermindCreator] = None
        self.all_history = {"Win": 0, "Lose": 0}

    def start_game(self, game_type: GameType):
        self.game_type = game_type
        if game_type == GameType.HIDDEN_SEQUENCE:
            self.mastermind_creator = HiddenSequenceMastermindCreator()
        elif game_type == GameType.MINE_SWEEPER:
            self.mastermind_creator = MineSweeperMastermindCreator()
        elif game_type == GameType.WAR:
            self.mastermind_creator = WarGameMastermindCreator()

    def parse_execute_input(self, input_string: str):
        """
        Parse user's raw input
        Args:
            input_string:
            Input format for Hidden Sequence game must be 4
            consecutive numbers e.g. "1234"

            Input format for minesweeper must be two numbers separated by column
            and spaces (if needed)
        """
        if input_string == "reset":
            self.mastermind_creator.reset()
        elif input_string == "clear":
            self.clear_all_history()
        elif self.game_type == GameType.HIDDEN_SEQUENCE \
                and input_string.isnumeric() and len(input_string) == 4:
            int_array = [int(i) for i in input_string]
            self.mastermind_creator.execute_input(int_array)
            self.update_all_history()
        elif self.game_type == GameType.MINE_SWEEPER:
            # Check if the input are two numbers separated by ','
            split_arr = [i.strip() for i in input_string.split(',')]
            if len(split_arr) == 2 and split_arr[0].isnumeric() and split_arr[1].isnumeric():
                int_array = [int(i) for i in split_arr]
                self.mastermind_creator.execute_input(int_array)
                self.update_all_history()
        elif self.game_type == GameType.WAR and input_string == "deal":
            self.mastermind_creator.execute_input([])
            self.update_all_history()

    def update_all_history(self):
        if self.mastermind_creator.get_game_state() == GameState.WIN:
            self.all_history["Win"] += 1
        elif self.mastermind_creator.get_game_state() == GameState.LOSE:
            self.all_history["Lose"] += 1

    def get_mastermind_local_history(self):
        return self.mastermind_creator.get_guess_history()

    def get_all_history(self):
        return self.all_history

    def clear_all_history(self):
        self.all_history = {"Win": 0, "Lose": 0}

    def get_display_data(self) -> str:
        if self.mastermind_creator:
            return self.mastermind_creator.get_display_string()
        else:
            return ""

    def get_game_state(self) -> GameState:
        return self.mastermind_creator.get_game_state()

    def end_game(self):
        self.game_type = None
        self.mastermind_creator = None
