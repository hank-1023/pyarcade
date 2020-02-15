from pyarcade.mastermind import Mastermind


class Client:
    def __init__(self):
        self.input_manager = InputManager()
        self.master_mind = Mastermind()

    def start(self, user_input: str):
        result_code, result_arr = self.input_manager.parse_input(user_input)
        if result_code == 2:
            self.master_mind.on_made_guess(result_arr)


class InputManager:
    def parse_input(self, user_input: str) -> (int, [int]):
        if user_input == "reset":
            return 0, []
        elif user_input == "clear":
            return 1, []
        else:
            # Check if all digits in input string are digits
            if user_input.isnumeric():
                int_array = [int(i) for i in user_input]
                return 2, int_array
            else:
                return -1, []
