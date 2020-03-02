import random

from pyarcade.imastermind import *


class HiddenSequenceMastermind(iMastermind):
    def __init__(self, game_size: int = 4, game_range: int = 10):
        super().__init__()
        self.sequence_length = game_size
        self.number_range = game_range
        self.current_hidden_sequence = self.generate_hidden_sequence()
        self.current_result = None

    def generate_hidden_sequence(self) -> [int]:
        """
        Returns:
            hidden_sequence List[int]: A sequence of integers to be guessed by the player.
        """
        return [random.randint(0, self.number_range) for _ in range(self.sequence_length)]

    def execute_input(self, game_input: [int]):
        self.guess_history.append(game_input)
        correct_indices = []
        misplaced_indices = []
        nowhere_indices = []
        for i, guess_digit in enumerate(game_input):
            if guess_digit == self.current_hidden_sequence[i]:
                correct_indices.append(i)
            elif guess_digit in self.current_hidden_sequence:
                misplaced_indices.append(i)
            else:
                nowhere_indices.append(i)

        self.current_result = correct_indices, misplaced_indices, nowhere_indices
        self.check_win()

    def check_win(self):
        if len(self.current_result[0]) == self.sequence_length:
            self.game_state = GameState.WIN

    def get_display_string(self) -> str:
        correct_digits = [x + 1 for x in self.current_result[0]]
        misplaced_digits = [x + 1 for x in self.current_result[1]]
        not_existed_digits = [x + 1 for x in self.current_result[2]]
        return "Correct digits: " + str(correct_digits) + "\n" \
               + "Misplaced digits: " + str(misplaced_digits) + "\n" \
               + "Numbers on these digits are not existed: " + str(not_existed_digits)

    def reset(self):
        self.current_hidden_sequence = self.generate_hidden_sequence()
        self.game_state = GameState.PENDING
        self.guess_history = []
