from enum import Enum
from typing import Optional, List
import random


class GameState(Enum):
    PENDING = 0
    WIN = 1
    LOSE = 2


class GameType(Enum):
    HIDDEN_SEQUENCE = 0
    MINESWEEPER = 1


class OpCode(Enum):
    RESET = 0
    CLEAR_HISTORY = 1
    HS_INPUT = 2
    MINESWEEPER_INPUT = 3


class Mastermind:
    """ A class representing a Mastermind game session

        Args:
            width (int): The number of random digits to generate

            max_range (int): The range that a single digit can vary

    """

    def __init__(self, game_type: GameType, width: Optional[int] = 4, max_range: Optional[int] = 10,
                 bomb_num: Optional[int] = 2):
        self.game_type = game_type
        self.width = width
        self.guess_history = []
        self.game_state = GameState.PENDING
        if game_type == GameType.HIDDEN_SEQUENCE:
            self.max_range = max_range
            self.current_hidden_sequence = self.generate_hidden_sequence()
        elif game_type == GameType.MINESWEEPER:
            self.bomb_num = bomb_num
            self.remain_count = width ** 2 - bomb_num
            self.game_matrix = self.generate_game_matrix()

    def generate_game_matrix(self) -> [[int]]:
        game_matrix = [[0 for _ in range(self.width)] for _ in range(self.width)]

        random_rows = random.sample(range(0, self.width), self.bomb_num)
        random_cols = random.sample(range(0, self.width), self.bomb_num)

        for row, col in zip(random_rows, random_cols):
            game_matrix[row][col] = 1

        return game_matrix

    def generate_hidden_sequence(self) -> List[int]:
        """
        Returns:
            hidden_sequence List[int]: A sequence of integers to be guessed by the player.
        """
        return [random.randint(0, self.max_range) for _ in range(self.width)]

    def on_user_input(self, op_code: OpCode, user_input: [int]):
        """
        Calls reset() or clear_history() if that's the desired operation
        Otherwise calls execute_hs_input()  and eval_hs() if it's a hidden_sequence input or
        execute_sweeper_input() and eval_sweeper() if it's a minesweeper input

        Args:
            op_code: Enum Op_Code indicates which operation to carry out
            user_input: The input array parsed by the input_system

        Returns:

        """
        if op_code == OpCode.RESET:
            self.reset()
        elif op_code == OpCode.CLEAR_HISTORY:
            self.clear_history()
        elif op_code == OpCode.HS_INPUT:
            feedback = self.execute_hs_input(user_input)
            self.eval_hs(feedback)
        elif op_code == OpCode.MINESWEEPER_INPUT and all(n < self.width for n in user_input):
            feedback = self.execute_sweeper_input(user_input)
            self.eval_sweeper(feedback)

    def execute_hs_input(self, user_input: [int]) -> ([int], [int], [int]):
        self.guess_history.append(user_input)
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
        if user_input in self.guess_history:
            return -1  # Already guessed
        self.guess_history.append(user_input)

        row, col = user_input[0], user_input[1]
        if self.game_matrix[row][col] == 1:
            return 0
        else:
            return 1

    def eval_hs(self, feedback: ([int], [int], [int])):
        """
        Evaluates the result of execution for hidden sequence inputs
        """
        if len(feedback[0]) == self.width:
            self.game_over(True)

    def eval_sweeper(self, feedback):
        """
        Evaluates the result of execution for mine sweeper inputs
        """
        if feedback == 0:
            self.game_over(False)
        elif feedback == 1:
            self.remain_count -= 1
            if self.remain_count == 0:
                self.game_over(True)

    def game_over(self, win: bool):
        """
        Changes the game_state if necessary
        """
        if win:
            self.game_state = GameState.WIN
        else:
            self.game_state = GameState.LOSE

    def reset(self):
        """
        regenerates game_matrix / sequence, reset counters and states and clear game history
        """
        if self.game_type == GameType.HIDDEN_SEQUENCE:
            self.current_hidden_sequence = self.generate_hidden_sequence()
        else:
            self.game_matrix = self.generate_game_matrix()
            self.remain_count = self.width ** 2 - self.bomb_num
        self.game_state = GameState.PENDING
        self.clear_history()

    def clear_history(self):
        self.guess_history = []
