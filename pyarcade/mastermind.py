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
        self.guess_history = []

    def generate_hidden_sequence(self) -> List[int]:
        """
        Returns:
            hidden_sequence List[int]: A sequence of integers to be guessed by the player.
        """
        return [random.randint(0, self.max_range) for _ in range(self.width)]

    def on_made_guess(self, guess: [int]):
        self.guess_history.append(guess)

