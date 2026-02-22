# Adversarial Search Engine: Algorithmic Simulation & Performance Analysis

## Overview

A Python simulation framework for benchmarking and profiling adversarial search algorithms in two-player, zero-sum games (Tic-Tac-Toe and Reversi/Othello). 

The engine pits different AI agents against each other in automated arenas across hundreds of trials, producing quantitative comparisons of algorithmic latency, pruning efficiency, and strategic dominance. It explores the strict computational trade-offs between deterministic brute-force search and probabilistic heuristic evaluation.

## Core Algorithms Implemented

### 1. Deterministic Search: Minimax & Alpha-Beta Pruning
The standard Minimax algorithm explores the entire game tree to find the mathematically optimal move. However, for games with larger state spaces, this becomes computationally unfeasible. 
* **Complexity:** Standard Minimax evaluates $O(b^d)$ nodes, where $b$ is the branching factor and $d$ is the depth.
* **Optimization:** The Alpha-Beta pruning variant dynamically eliminates branches that cannot influence the final decision, significantly reducing the effective branching factor and allowing deeper search within the same time budget.



### 2. Probabilistic Search: Monte Carlo Tree Search (MCTS)
MCTS diverges from deterministic search by relying on randomized simulations (rollouts) to evaluate the potential of a given move. It balances **exploration** (trying new moves) and **exploitation** (focusing on moves with a high historical win rate) using the Upper Confidence Bound (UCB1) formula:

$$
UCB1 = \frac{w_i}{n_i} + c \sqrt{\frac{\ln N_i}{n_i}}
$$

(Where $w_i$ is the number of wins, $n_i$ is the node visits, $N_i$ is the parent visits, and $c$ is the exploration parameter).



### 3. Heuristic Approximation: Depth-Limited Minimax
In Reversi, the theoretical state space is roughly $O(10^{28})$, making terminal search impossible. The depth-limited variant introduces a **custom heuristic evaluation function** to approximate the utility of non-terminal states. 
* **Reversi Heuristics:** The evaluation function scores board states using a composite of *Coin Parity*, *Mobility* (number of legal moves), *Corner Captures*, *Corner Proximity*, and a static *Positional Stability Matrix* — each with empirically tuned weights.



## Simulation & Benchmarking Engine

The core of this project is the simulation engine (`main.py`), which orchestrates automated matchups between different AI agents over configurable trial counts. 

**Tracked Metrics:**
* **Win/Loss/Draw Rates:** Evaluates the strategic dominance of a given algorithm.
* **Computational Latency:** Tracks the exact execution time per move (`Average_Move_Time`), providing a quantitative measure of algorithmic efficiency and overhead.

### Benchmark Results

| Game Environment | Algorithm (Player 1) | Algorithm (Player 2) | Win / Loss / Draw | Avg Move Time (P1) | Avg Move Time (P2) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tic-Tac-Toe** | **Minimax (Pruning)** | Random | 100 / 0 / 0 | 0.0100s | 0.0000s |
| **Tic-Tac-Toe** | MCTS | Random | 96 / 4 / 0 | 0.0150s | 0.0000s |
| **Tic-Tac-Toe** | Minimax (Standard) | **Minimax (Pruning)** | 0 / 0 / 100 | 0.1865s | **0.0011s** |
| **Reversi** | **MCTS** | Limited Pruning | 12 / 4 / 4 | 13.8621s | **0.0655s** |

### Key Algorithmic Insights
1. **Pruning Impact:** In Tic-Tac-Toe, Alpha-Beta Pruning achieved the exact same theoretical outcome (perfect draw) as Standard Minimax but was approximately **170x faster** (0.0011s vs 0.1865s). Same decision quality, drastically lower compute.
2. **Accuracy vs. Latency in Large State Spaces:** In Reversi, MCTS proved strategically superior (60% win rate) but required ~212x more compute per move (13.86s vs 0.065s) compared to the heuristic-based agent. This illustrates the fundamental trade-off between search depth and wall-clock constraints.

## Project Architecture

The codebase relies on strict Object-Oriented encapsulation, separating game environments from decision-making agents:
* **`game.py`**: Abstract base class defining environment constraints, state transitions, and utility functions.
* **Environments**: `tictactoe.py` and `reversi.py` inherit from the base class to implement specific state spaces.
* **Agents**: Individual modules (`mcts.py`, `minimax_pruning.py`, `minimax_limited_pruning.py`) contain isolated algorithmic strategy logic.

## Installation & Usage

1. **Prerequisites:** Python 3.x, `numpy`
2. **Execute Engine:** 
```bash
python main.py
```

3. Follow the interactive prompts to select the game environment, assign agent algorithms to Player 1 and Player 2, and define the simulation trial count. Performance statistics will print to the console upon completion.

## License

This project is open-source and available under the [MIT License](LICENSE.md).
