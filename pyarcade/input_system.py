from pyarcade.mastermind import *


class InputManager:
    """ A class managing all user inputs """
    def __init__(self, game_type: GameType):
        self.mastermind = Mastermind(game_type=game_type)
        self.game_type = game_type

    def parse_input(self, input_string: str):
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
            self.mastermind.on_user_input(OpCode.RESET, None)
        elif input_string == "clear":
            self.mastermind.on_user_input(OpCode.CLEAR_HISTORY, None)
        # Check if all digits in input string are 4 digits
        elif self.game_type == GameType.HIDDEN_SEQUENCE and input_string.isnumeric() and len(input_string) == 4:
            int_array = [int(i) for i in input_string]
            self.mastermind.on_user_input(OpCode.HS_INPUT, int_array)
        elif self.game_type == GameType.MINESWEEPER:
            # Check if the input are two numbers separated by ','
            split_arr = [i.strip() for i in input_string.split(',')]
            if len(split_arr) == 2 and split_arr[0].isnumeric() and split_arr[1].isnumeric():
                int_array = [int(i) for i in split_arr]
                self.mastermind.on_user_input(OpCode.MINESWEEPER_INPUT, int_array)
        else:
            return
