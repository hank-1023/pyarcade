from pyarcade.mastermind import Mastermind


class InputManager:
    """ A class managing all user inputs """
    def __init__(self, game_type: int):
        self.mastermind = Mastermind(game_type=game_type)
        self.game_type = game_type

    def parse_input(self, input_string: str):
        if input_string == "reset":
            self.mastermind.on_user_input((0, []))
        elif input_string == "clear":
            self.mastermind.on_user_input((1, []))
        # Checking if all digits in input string are 4 digits
        elif self.game_type == 0 and input_string.isnumeric() and len(input_string) == 4:
            int_array = [int(i) for i in input_string]
            self.mastermind.on_user_input((2, int_array))
        elif self.game_type == 1:
            split_arr = input_string.split(",")
            if len(split_arr) == 2 and split_arr[0].isnumeric() and split_arr[1].isnumeric():
                int_array = [int(i) for i in input_string]
                self.mastermind.on_user_input((3, int_array))
        else:
            return
