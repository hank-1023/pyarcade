from typing import Optional, List
import random


class Mastermind:
    """ A class representing a Mastermind game session

        Args:
            width (int): The number of random digits to generate

            max_range (int): The range that a single digit can vary

    """
    def __init__(self, width: Optional[int] = 4, max_range: Optional[int] = 10):
        self.width = width
        self.max_range = max_range
        self.current_hidden_sequence = self.generate_hidden_sequence()
        self.guess_history = []

    def generate_hidden_sequence(self) -> List[int]:
        """
        Returns:
            hidden_sequence List[int]: A sequence of integers to be guessed by the player.
        """
        return [random.randint(0, self.max_range) for _ in range(self.width)]

    def on_made_guess(self, guess_arr: [int]) -> ([int], [int], [int]):
        """
        Args:
            guess_arr: the user's guess

        Returns:
            the indices where the user has the correct guess, incorrect but somewhere in the hidden_sequence,
            and those which are not existed in hidden_sequence
        """
        self.guess_history.append(guess_arr)
        correct_indices = []
        misplaced_indices = []
        nowhere_indices = []
        for i, guess_digit in enumerate(guess_arr):
            if guess_digit == self.current_hidden_sequence[i]:
                correct_indices.append(i)
            elif guess_digit in self.current_hidden_sequence:
                misplaced_indices.append(i)
            else:
                nowhere_indices.append(i)

        return correct_indices, misplaced_indices, nowhere_indices

    def reset(self):
        self.current_hidden_sequence = self.generate_hidden_sequence()
        self.clear_history()

    def clear_history(self):
        self.guess_history = []
