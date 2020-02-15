from pyarcade.mastermind import Mastermind
from sys import stdin


class Client:
    """ A backend client that connect functionality of InputManager and Mastermind """
    def __init__(self, file):
        self.input_manager = InputManager()
        self.master_mind = Mastermind()
        self.file = open(file, 'r')

    def start(self) -> bool:
        lines = self.file.read().splitlines()
        for line in lines:
            if not line:
                continue
            result_code, result_arr = self.input_manager.parse_input(line)
            if result_code == 0:
                self.master_mind.reset()
                print("Game Reset!")
            elif result_code == 1:
                self.master_mind.clear_history()
                print("History cleared!")
            elif result_code == 2:
                correct, misplaced, nowhere = self.master_mind.on_made_guess(result_arr)
                if len(correct) == 4:
                    print("All indices correct!")
                    self.file.close()
                    return True
                if correct:
                    print("Correct indices are:")
                    print(correct)
                if misplaced:
                    print("Misplaced indices are:")
                    print(misplaced)
                if nowhere:
                    print("Those indices do not exists in sequence:")
                    print(nowhere)
                print("Please try again")
            elif result_code == -1:
                print("Please check and input 4 digits")
        self.file.close()
        return False


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
            if user_input.isnumeric() and len(user_input) == 4:   # Checking if all digits in input string are 4 digits
                int_array = [int(i) for i in user_input]
                return 2, int_array
            else:
                return -1, []
