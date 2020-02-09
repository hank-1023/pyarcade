# PyArcade -- The Back End Test Suite

# Software Requirements
These are the following requirements for your implementation of PyArcade.

## Input System
NOTE: Requirements to STORE something does **not** mean it needs to be persistent across restarts of the system.

1. The *input_system* **MUST** ignore all inputs that do not have meaningful functionality for *Mastermind*.
2. The *input_system* **MUST** parse a string of integers of the appropriate size into an input that *Mastermind* can use.
3. The *input_system* **MUST** reset a game of *Mastermind* to the starting state if the string "reset" is provided.
4. The *input_system* **MUST** clear the game history of *Mastermind* if the string "clear" is provided.

## Mastermind (Cows and Bulls)
1. *Mastermind* **MUST** generate a random hidden sequence of 4 numbers from 0 to 9 (inclusive). 
2. *Mastermind* **MUST** accept as input from the user a guessed sequence, 4 numbers from 0 to 9 (inclusive).
3. *Mastermind* **MUST** output an *evaluation.* This includes for each digit in the guessed sequence, whether that digit is:
    1. Nowhere in the hidden sequence at all 
    2. Somewhere in the hidden sequence, but not in the location it was submitted
    3. Is in the hidden sequence at the location it was submitted. 

4. *Mastermind* **MUST** store history of all of the guessed sequences and the evaluation for the current session.
5. *Mastermind* **MUST** store the entire history once the current guessed sequence matches the hidden sequence exactly.

## Testing Requirements
For this project, you must have > 97% code-coverage using your test-suite. 
To test the coverage of your unit-tests, use [pytest-cov](https://pypi.org/project/pytest-cov/).
 