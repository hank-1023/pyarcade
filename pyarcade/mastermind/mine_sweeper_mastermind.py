import random
from pyarcade.mastermind.mastermind import *


class MineSweeperMastermind(iMastermind):
    def __init__(self, bomb_num: int = 2, board_size: int = 4):
        super().__init__()
        self.bomb_num = bomb_num
        self.board_size = board_size
        self.game_matrix = self.init_game_matrix()
        self.display_board = [["x" for _ in range(self.board_size)] for _ in range(self.board_size)]

    def init_game_matrix(self) -> [[int]]:
        """
        Returns:
        game_matrix: indicates proximity to bombs and bomb location, -1 means bomb,
        other numbers indicate proximity
        The matrix has len=board_size + 2 in order to make corner case easier to check

        The true index of game board is from 1 to self.board_size
        """
        game_matrix = [[0 for _ in range(self.board_size + 2)] for _ in range(self.board_size + 2)]

        random_rows = random.sample(range(1, self.board_size + 1), self.bomb_num)
        random_cols = random.sample(range(1, self.board_size + 1), self.bomb_num)

        for row, col in zip(random_rows, random_cols):
            game_matrix[row][col] = -1

        for row in range(1, self.board_size + 1):
            for col in range(1, self.board_size + 1):
                if game_matrix[row][col] == -1:
                    continue
                for rr in range(row - 1, row + 2):
                    for cc in range(col - 1, col + 2):
                        if game_matrix[rr][cc] == -1:
                            game_matrix[row][col] += 1
        return game_matrix

    def execute_input(self, game_input: [int]):
        """
        Args:
            game_input: list with len = 2: row, column to detonate the bomb
        """
        if not all(n < self.board_size for n in game_input):
            raise ValueError("input outside of board_range")

        # Add to guess history
        if game_input not in self.guess_history:
            self.guess_history.append(game_input)

        row, col = game_input[0], game_input[1]
        if self.game_matrix[row+1][col+1] != -1:
            self.display_board[row][col] = str(self.game_matrix[row + 1][col + 1])
        else:
            # Shows the user has stepped on bomb
            self.display_board[row][col] = "*"
            self.game_state = GameState.LOSE

        self.check_win()

    def check_win(self):
        if self.game_state == GameState.LOSE:
            self.all_history["Lose"] += 1
            return

        if sum(sublist.count("x") for sublist in self.display_board) == self.bomb_num:
            self.game_state = GameState.WIN
            self.all_history["Win"] += 1

    def get_display_data(self):
        return self.display_board

    def reset(self):
        self.game_matrix = self.init_game_matrix()
        self.display_board = [["x" for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.game_state = GameState.PENDING
        self.guess_history = []
