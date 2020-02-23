# Assignment 4 README
## Changes in input_system to adapt for new game
* Deleted Client class since inputs are now passed as function parameters
* add “game_type” to init
* parse_input now accept mine_sweeper inputs and pass op_code = MINESWEEPER_INPUT into mastermind as a signal for minesweeper inputs

## Refactorings after development
* Most primitives which represent categorical values are now factored out as various enum values: GameState, GameType, OpCode to improve readability and avoid errors
* In order to avoid large method: on_made_guess now renamed to on_user_input and only process operation code parsed by input_system and call other functions to carry out the operation
	* As a result, previous functionalities for hidden_sequence game are refactored out as a new function: execute_hs_input() and eval_hs() would be called to process the execution result
* Some module test methods are too long, so some aren’t necessarily together are extracted as another function to test specific scenario, such as: test_minesweeper_success
* Client class are removed to avoid bilateral connection between Mastermind and Client