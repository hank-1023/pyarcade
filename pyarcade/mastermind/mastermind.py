from enum import Enum


class GameState(Enum):
    PENDING = 0
    WIN = 1
    LOSE = 2


class OpCode(Enum):
    RESET = 0
    CLEAR_HISTORY = 1
    VALID_INPUT = 2


class Mastermind:
    """
    Product interface. Can be subclassed to concrete products to be used in actual games
    """
    def __init__(self):
        self.game_state = GameState.PENDING
        self.guess_history = []

    def on_user_input(self, op_code: OpCode, game_input: [int]):
        """
        Controller of Mastermind functions.
        """
        if op_code == OpCode.RESET:
            self.reset()
        elif op_code == OpCode.CLEAR_HISTORY:
            self.clear_history()
        elif op_code == OpCode.VALID_INPUT:
            self.execute_input(game_input)
            self.check_win()
            self.update_ui()

    def game_over(self, win: bool):
        """
        Changes the game_state if necessary
        """
        if win:
            self.game_state = GameState.WIN
        else:
            self.game_state = GameState.LOSE

    def clear_history(self):
        self.guess_history = []

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
        """
        raise NotImplementedError

    def update_ui(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError
