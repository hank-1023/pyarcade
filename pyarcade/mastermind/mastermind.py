from enum import Enum


class GameState(Enum):
    PENDING = 0
    WIN = 1
    LOSE = 2
    TIE = 3


class iMastermind:
    """
    Product interface. Can be subclassed to concrete products to be used in actual games
    """
    def __init__(self):
        self.game_state = GameState.PENDING
        self.guess_history = []
        self.all_history = {"Win": 0, "Lose": 0}

    def execute_input(self, game_input: [int]):
        """

        Args:
            game_input: the parsed game input
        Returns:

        """
        raise NotImplementedError

    def check_win(self):
        """
        Called by on_user_input after execute_input() to check if user has won the game
        Should update self.game_state
        """
        raise NotImplementedError

    def get_display_data(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def clear_history(self):
        self.all_history = {"Win": 0, "Lose": 0}

