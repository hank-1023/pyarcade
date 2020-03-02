# PyArcade

## Assignment 4 Approximate Work Distribution

1. Zizhou Wang: 60% effort
    1. Implemented factory method architecture for mastermind
    2. Redo all 3 masterminds to implement the new interface
    3. Added Client class as the IO interface for backend
    3. Added tests for the 3 masterminds and Client class
    
2. Chenhao Huang: 40% effort
    1. Designed UI and implemented all UI elements
    2. Wrote tests for UI

## Design Pattern
We chose to use the **factory method** architecture because:
* It provides an abstraction between Mastermind classes and Client so Client doesn't need to
know specific details of each mastermind but is still able to do all necessary operations
* It organizes the fragmented implementations of different Masterminds
* It makes it easy to add a new game in the future as long as the new game's mastermind
implements the iMastermind interface

You can see where we used it in **pyarcade/mastermind_factory.py** and **pyarcade/imastermind.py**  

The concrete products are in **pyarcade/mastermind** module

As a minified example: 

```Python
from pyarcade.mastermind.hidden_sequence_mastermind import *
from pyarcade.mastermind.war_mastermind import *

# The Creator class
class iMastermindCreator:
    def __init__(self):
        self.mastermind = self.create_mastermind()

    # The factory method
    def create_mastermind(self) -> iMastermind:
        raise NotImplementedError

    # The default implementations of all necessary functions
    # Calls methods from the created mastermind create_mastermind()
    def execute_input(self, game_input: [int]):
        self.mastermind.execute_input(game_input)

# Example of the concrete creator classes
class HiddenSequenceMastermindCreator(iMastermindCreator):
    def create_mastermind(self) -> HiddenSequenceMastermind:
        return HiddenSequenceMastermind()

# Interface for concrete products
class iMastermind:
    def __init__(self):
        self.game_state = GameState.PENDING
        self.guess_history = []

    def execute_input(self, game_input: [int]):
        raise NotImplementedError

# Example of the concrete product
class HiddenSequenceMastermind(iMastermind):
    def __init__(self, game_size: int = 4, game_range: int = 10):
        super().__init__()
        self.sequence_length = game_size
        self.number_range = game_range
        self.current_hidden_sequence = self.generate_hidden_sequence()
        self.current_result = None
```
As you can see from the code above, with the benefit of abstractions, 
the Client class now doesn't need to know the specific details of *HiddenSequenceMastermind* or 
even *HiddenSequenceMastermindCreator* since *iMastermindCreator* guarantees certain functionality
```Python
from pyarcade.client import *

client = Client()
client.mastermind_creator = HiddenSequenceMastermindCreator()
client.mastermind_creator.execute_input([1, 2, 3, 4])

client.mastermind_creator = MineSweeperMastermindCreator()
client.mastermind_creator.execute_input([1, 1])
```
