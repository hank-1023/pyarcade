from pyarcade.mastermind import Mastermind


class Client:
    def __init__(self):
        self.input_manager = InputManager(self)
        self.master_mind = Mastermind()

    def add_guess(self, guess: [int]):
        self.master_mind.on_guess_made(guess)


class InputManager:
    def __init__(self, client: Client):
        self.client = client

    def parse_input(self, user_input: str):
        if user_input == "reset":
            # reset the game
            pass
        elif user_input == "clear":
            # clear the game
            pass
        else:
            if user_input.isnumeric():
                int_array = [int(i) for i in user_input]
                self.client.add_guess(int_array)
            else:
                print("Input is not a sequence of number")
