from pyarcade.mastermind import Mastermind
from sys import stdin


class Client:
    """ A backend client that connect functionality of InputManager and Mastermind """
    def __init__(self):
        self.input_manager = InputManager()
        self.master_mind = Mastermind()

    def start(self):
        print("Please start guessing: ")
        while True:
            line = stdin.readline().rsplit()[0]
            result_code, result_arr = self.input_manager.parse_input(line)
            if result_code == 2:
                print(self.master_mind.on_made_guess(result_arr))


class InputManager:
    """ A class managing all user input

        Returns: (int, [int]) as result code and parsed array (if any)
    """
    def parse_input(self, user_input: str) -> (int, [int]):
        if user_input == "reset":
            return 0, []
        elif user_input == "clear":
            return 1, []
        else:
            if user_input.isnumeric():   # Checking if all digits in input string are 4 digits
                int_array = [int(i) for i in user_input]
                return 2, int_array
            else:
                return -1, []
