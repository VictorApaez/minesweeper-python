# Minesweeper in Python

Minesweeper is a classic puzzle game implemented using Python, Tkinter, and Object-Oriented Programming (OOP). This project follows the principles of Test-Driven Development (TDD), with each class and its methods tested using pytest.

## Description

This implementation of Minesweeper provides an engaging and interactive user experience. The game is divided into different classes representing the key components: `Cell`, `Board`, and `Game`. The user interface is designed using Tkinter.

## Code Overview

### Object-Oriented Programming (OOP)

The following OOP principles are demonstrated in this project:

1. **Encapsulation**: The classes `Cell`, `Board`, and `Game` encapsulate their respective properties and methods, providing a clear structure and hiding the internal implementation from other parts of the code.
   Example: `Cell` class encapsulates properties like `is_mine`, `is_revealed`, `is_flagged`, etc.

2. **Inheritance**: While there's no direct inheritance between custom classes, the usage of exceptions (e.g., `MineRevealedError`) shows a form of inheritance from Python's base `Exception` class.

3. **Polymorphism**: The usage of a callback function in `reveal_cell` method allows for different implementations for updating the UI, thus demonstrating polymorphism.

4. **Abstraction**: The `Game` class provides higher-level methods like `start_game`, `reveal_cell`, etc., abstracting the underlying details from the user interface.

## Features

- Interactive GUI using Tkinter
- Flagging mines
- Revealing cells
- End game scenarios (win/loss detection)
- Time tracking

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/VictorApaez/minesweeper-python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd minesweeper-python
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Using the App

Run `main.py` from the project directory to start the game:

```bash
python main.py
```

## Testing the App

The project uses pytest for testing. All classes and their methods are thoroughly tested.

1. Navigate to the project directory.
2. Run the tests:
   ```bash
   pytest
   ```

## Contact

Feel free to reach out with any questions or feedback:

- Email: [vic.apaez@gmail.com](mailto:vic.apaez@gmail.com)

## Contributing

Contributions are welcome! Please create an issue or submit a pull request on [GitHub](https://github.com/VictorApaez/minesweeper-python).
