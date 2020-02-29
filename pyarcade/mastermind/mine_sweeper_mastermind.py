from random import random
from pyarcade.mastermind.mastermind import *


class MineSweeperMastermind(Mastermind):
    def __init__(self, bomb_num: int = 2, board_size: int = 4):
        super().__init__()
        self.bomb_num = bomb_num
        self.board_size = board_size
        self.remain_count = board_size ** 2 - bomb_num
        self.game_matrix = self.generate_game_matrix()

    def generate_game_matrix(self) -> [[int]]:
        game_matrix = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]

        random_rows = random.sample(range(0, self.board_size), self.bomb_num)
        random_cols = random.sample(range(0, self.board_size), self.bomb_num)

        for row, col in zip(random_rows, random_cols):
            game_matrix[row][col] = 1

        return game_matrix

    def execute_input(self, game_input: [int]) -> int:
        """
        TODO: Should modify game state instead
        Args:
            game_input:

        Returns:

        """
        if not all(n < self.board_size for n in game_input):
            raise ValueError("input outside of board_range")

        if game_input in self.guess_history:
            return -1  # Already guessed
        self.guess_history.append(game_input)

        row, col = game_input[0], game_input[1]
        if self.game_matrix[row][col] == 1:
            return 0
        else:
            return 1

    def check_win(self):
        raise NotImplementedError

    def update_ui(self):
        raise NotImplementedError

    def reset(self):
        self.game_matrix = self.generate_game_matrix()
        self.remain_count = self.board_size ** 2 - self.bomb_num
        self.game_state = GameState.PENDING
        self.clear_history()
