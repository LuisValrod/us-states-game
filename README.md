# U.S. States Game

This is a simple U.S. states identification game using the Turtle library in Python.

## Requirements

- Python 3.x
- Python libraries: `turtle`, `pandas`

## Description

The game loads a map of the U.S. and displays a dialog box prompting the player to type in the name of a state. If the entered state name is correct, it is shown on the map and another state is prompted. The game continues until all 50 states are guessed or until the player types "Exit".

## Usage Instructions

1. Run the `us_states_game.py` script.
2. A window will open displaying a map of the U.S. with the states blanked out.
3. Type in the name of a state when prompted in the console.
4. If the state name is correct, it will be shown on the map and another state will be prompted.
5. Repeat steps 3 and 4 until you've guessed all the states or type "Exit" to quit the game.
6. If you exit the game before guessing all the states, a `states_to_learn.csv` file will be generated containing the states you still need to guess.

## Files

- `us_states_game.py`: The main script that runs the game.
- `50_states.csv`: CSV file containing the data of U.S. states.
- `blank_states_img.gif`: Image of the blank map of the U.S.
- `states_to_learn.csv`: Generated CSV file containing the states that still need to be guessed.

## Credits

This project was created by Luis Rodriguez.
