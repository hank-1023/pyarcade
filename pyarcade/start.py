from pyarcade.input_system import *


def run_pyarcade(game_type: GameType):
    """ This will effectively become our program entrypoint.
    """
    input_manager = InputManager(game_type)


if __name__ == "__main__":
    run_pyarcade(GameType.HIDDEN_SEQUENCE)
