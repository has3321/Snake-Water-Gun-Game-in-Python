# Snake-Water-Gun-Game-in-Python

# Snake, Water, Gun Game

This is a simple Python-based implementation of the classic Snake, Water, Gun game, where the user competes against the computer. The computer makes a random choice, and the user inputs their choice to see who wins!

## Game Rules

- The game is played between two entities: the user and the computer.
- The user has three options to choose from:
  - `s` for Snake
  - `w` for Water
  - `g` for Gun

The game's outcome is determined as follows:

- Snake beats Gun.
- Gun beats Water.
- Water beats Snake.
- If both the user and the computer make the same choice, it’s a draw.

## Code Walkthrough

### Input:
- The program asks the user to input one of the three options: `s`, `w`, or `g`.
- The computer randomly selects one of the three options.

### Logic:
- A dictionary (`yourdict`) is used to map the choices (`s`, `w`, `g`) to numbers:
  - `1` represents Snake
  - `0` represents Gun
  - `-1` represents Water
- The computer’s and user’s choices are then compared using conditional statements to determine the winner:
  - If both choices are the same, the result is a draw.
  - If the choices are different, the winner is decided based on the rules mentioned above.

### Output:
- The program displays the choices of both the user and the computer, and prints the result: "You win!", "You lose!", or "Match Draw".

## How to Run the Game

### Prerequisites:
- Python 3.x

### Steps:
1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/snake-water-gun.git
