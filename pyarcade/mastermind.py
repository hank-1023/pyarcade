from typing import Optional, List
import random


class Mastermind:
    """ A class representing a Mastermind game session

        Args:
            width (int): The number of random digits to generate

            max_range (int): The range that a single digit can vary

    """
    def __init__(self, game_type: int, width: Optional[int] = 4, max_range: Optional[int] = 10):
        self.width = width
        self.max_range = max_range
        if game_type == 0:
            self.current_hidden_sequence = self.generate_hidden_sequence()
        elif game_type == 1:
            self.game_matrix = self.generate_game_matrix()
        self.guess_history = []

    def generate_game_matrix(self) -> [[int]]:
        pass

    def generate_hidden_sequence(self) -> List[int]:
        """
        Returns:
            hidden_sequence List[int]: A sequence of integers to be guessed by the player.
        """
        return [random.randint(0, self.max_range) for _ in range(self.width)]

    def on_user_input(self, user_input: (int, [int])):
        """

        Args:
            user_input:

        Returns:

        """
        self.guess_history.append(user_input)
        if user_input[0] == 0:
            self.reset()
        elif user_input[0] == 1:
            self.clear_history()
        elif user_input[0] == 2:
            self.execute_hs_input(user_input[1])
        elif user_input[0] == 3:
            self.execute_sweeper_input(user_input[1])

    def execute_hs_input(self, user_input: [int]) -> ([int], [int], [int]):
        correct_indices = []
        misplaced_indices = []
        nowhere_indices = []
        for i, guess_digit in enumerate(user_input):
            if guess_digit == self.current_hidden_sequence[i]:
                correct_indices.append(i)
            elif guess_digit in self.current_hidden_sequence:
                misplaced_indices.append(i)
            else:
                nowhere_indices.append(i)

        return correct_indices, misplaced_indices, nowhere_indices

    def execute_sweeper_input(self, user_input: [int]) -> int:
        pass



    def reset(self):
        self.current_hidden_sequence = self.generate_hidden_sequence()
        self.clear_history()

    def clear_history(self):
        self.guess_history = []
