# Rock Paper Scissors

A simple **Rock Paper Scissors game built with Python**.

The game supports two modes:

- **Single Player** — Play against the computer.
- **Multiplayer** — Two players can play against each other.

This project is a simple way to practice Python fundamentals such as conditionals, loops, lists, dictionaries, user input, and the `random` module.

---

## Features

- Single-player mode against the computer
- Two-player multiplayer mode
- Random computer moves
- Input validation
- Replay option
- Simple Rock Paper Scissors game logic

---

## Requirements

You only need **Python 3** installed on your computer.

Check whether Python is installed:

```bash
python3 --version
```

---

## How to Run

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd <project-folder>
```

Run the game:

```bash
python3 main.py
```

Replace `main.py` with your Python filename if it is different.

---

## How to Play

When the game starts, choose a game mode:

```text
Type Single / Multi:
```

### Single Player

Enter one of the following:

```text
rock
paper
scissors
```

The computer will randomly choose its move.

The normal Rock Paper Scissors rules apply:

```text
Rock     beats Scissors
Paper    beats Rock
Scissors beats Paper
```

### Multiplayer

Player 1 enters their move first.

The screen is then filled with blank lines so Player 2 cannot easily see Player 1's choice.

Player 2 enters their move, and the game determines the winner.

---

## Game Logic

The winning combinations are stored in a dictionary:

```python
beats = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}
```

For example:

```python
beats["rock"]
```

returns:

```text
scissors
```

This means **Rock beats Scissors**.

Using a dictionary makes the game logic simpler and avoids writing many nested `if/elif` statements.

---

## Concepts Used

This project demonstrates several basic Python concepts:

- Variables
- User input with `input()`
- Conditional statements (`if`, `elif`, `else`)
- `while` loops
- Lists
- Dictionaries
- Membership operators (`in`, `not in`)
- `random.choice()`
- String methods such as `.lower()`
- f-strings

---

## Possible Improvements

Some features that could be added in the future:

- Keep track of player scores
- Add best-of-3 or best-of-5 matches
- Allow players to enter their names
- Split the program into functions
- Improve multiplayer screen hiding
- Create a graphical interface (GUI)
- Add online multiplayer

---

## Author

Created by **Dev Nirwal**