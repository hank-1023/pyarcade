from pyarcade.input_system import Client


def run_pyarcade():
    """ This will effectively become our program entrypoint.
    """
    client = Client()
    client.start()


if __name__ == "__main__":
    run_pyarcade()
