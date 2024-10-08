# AI-Game-Strategies

## Overview

This project involves the development of AI players for classic board games such as **Tic-Tac-Toe** and **Reversi (Othello)**. By implementing various artificial intelligence algorithms, including Minimax and Monte Carlo Tree Search (MCTS), the project demonstrates how AI can be applied to game strategies, providing both challenging opponents and insights into game AI development.

## Tools Used

- **Python**: The primary programming language used for implementing the game logic and AI algorithms.
- **NumPy**: Utilized for numerical operations, particularly in the Minimax algorithm.

## Objectives

- To implement classic board games with a focus on AI development.
- To explore and compare different AI algorithms for game playing:
  - **Random Player**: Makes random valid moves.
  - **Manual Player**: Allows human interaction through the command line.
  - **Minimax Player**: Implements the Minimax algorithm for optimal decision-making.
  - **Minimax with Pruning Player**: Enhances Minimax with alpha-beta pruning for efficiency.
  - **Minimax with Limited Pruning Player**: Introduces depth limits to the Minimax algorithm.
  - **Monte Carlo Tree Search Player**: Utilizes MCTS for decision-making in games with larger state spaces.
- To provide a platform for simulating games between different AI strategies and analyzing their performance.

## Project Structure

The project is organized into several Python scripts, each responsible for different aspects of the games and AI players. Below is an overview of each file:

### `game.py`

- **Description**: Contains the base classes and methods shared by all games, such as the game state, move generation, and utility calculation.
- **Key Components**:
  - Abstract game class defining the common interface for games.
  - Methods for initializing game states and validating moves.

### `main.py`

- **Description**: The entry point of the application, allowing users to select the game, players, and number of simulations.
- **Features**:
  - Interactive menu for game and player selection.
  - Simulation of multiple games with statistical output of results.
- **Usage**:
  - Run `main.py` and follow the prompts to start playing or simulating games.

### `manual_player.py`

- **Description**: Enables a human player to participate in the game via the command line.
- **Functionality**:
  - Prompts the user for input and validates the entered moves.
  - Integrates seamlessly with the game loop for human interaction.

### `randomplayer.py`

- **Description**: Implements a player that selects moves at random.
- **Purpose**:
  - Serves as a baseline for AI performance comparison.
  - Useful for testing and simulating games without strategic input.

### `minimax.py`

- **Description**: Implements the Minimax algorithm for optimal decision-making in games.
- **Algorithm Details**:
  - Recursively explores all possible moves to determine the best outcome.
  - Suitable for games with smaller state spaces like Tic-Tac-Toe.
- **Function**:
  - `minimax_player(game, state)`: Returns the best move determined by Minimax.

### `minimax_pruning.py`

- **Description**: Enhances the Minimax algorithm with alpha-beta pruning to improve efficiency.
- **Benefits**:
  - Reduces the number of nodes evaluated in the game tree.
  - Speeds up decision-making without sacrificing optimality.

### `minimax_limited_pruning.py`

- **Description**: Introduces a depth limit to the Minimax algorithm with pruning.
- **Use Case**:
  - Balances between computational efficiency and decision quality.
  - Useful for games with larger state spaces where full depth exploration is impractical.

### `mcts.py`

- **Description**: Implements the Monte Carlo Tree Search algorithm.
- **Algorithm Details**:
  - Uses random simulations to evaluate moves.
  - Balances exploration and exploitation to make decisions.
- **Functionality**:
  - `MCTSNode`: Class representing nodes in the MCTS tree.
  - `mcts_player(game, state, iterations=2000)`: Determines the best move using MCTS.

### `tictactoe.py`

- **Description**: Contains the implementation of the Tic-Tac-Toe game logic.
- **Features**:
  - Game state representation.
  - Move generation and validation.
  - Utility calculation to determine game outcomes.

### `reversi.py`

- **Description**: Contains the implementation of the Reversi (Othello) game logic.
- **Features**:
  - Handles more complex game rules compared to Tic-Tac-Toe.
  - Supports larger board sizes and more strategic depth.

## How to Run the Project

1. **Install Python**: Ensure Python 3.x is installed on your system.

2. **Install Dependencies**: Install NumPy if you plan to use algorithms that require it.
   ```bash
   pip install numpy

3. **Run the Main Script**:
    ```bash
    python main.py
  - Follow the on-screen prompts to select the game, players, and number of games to simulate.

## Features

  - **Interactive Gameplay**: Play against various AI opponents or watch AI players compete against each other.
  - **Multiple AI Strategies**: Compare different AI algorithms and observe their decision-making processes.
  - **Performance Statistics**: After simulations, view statistics such as win rates and average move times.

## Project Highlights

  - **Modular Design**: Each AI strategy and game logic is encapsulated in separate modules for clarity and reusability.
  - **Algorithm Implementation**: Demonstrates practical implementations of key AI algorithms in game playing.
  - **Extensibility**: The project structure allows for easy addition of new games or AI strategies.

## License

This project is open-source and available under the MIT License.

> **Note:** The code provided in this project is intended for educational purposes, showcasing the implementation of AI algorithms in game playing. While efforts have been made to ensure the correctness of the algorithms, they may not represent the most optimized or advanced versions available.
