import copy
import math
import random

class MCTSNode:
    def __init__(self, game, game_state, parent=None, move=None):
        """
        Initialize a node for Monte Carlo Tree Search.
        
        Args:
            game: The game being played.
            game_state: The current state of the game.
            parent: The parent node.
            move: The move that led to this node.
        """
        self.game = game
        self.state = copy.deepcopy(game_state)
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0
        self.move = move
        self.unexplored_moves = list(self.state.moves)
        self.player = game_state.to_move

    def selection(self):
        """
        Select a child node with the highest UCB1 value.

        Returns:
            MCTSNode: The selected child node.
        """
        c = 1.4
        log_visit_count = math.log(self.visits) if self.visits > 0 else 0
        
        def ucb1(child):
            if child.visits == 0:
                return float('inf')
            else:
                return (child.wins / child.visits) + c * math.sqrt(log_visit_count / child.visits)

        return max(self.children, key=ucb1)

    def expansion(self):
        """
        Expand the node by adding all possible child nodes.
        """
        for move in self.unexplored_moves:
            new_state = self.game.result(self.state, move)
            child_node = MCTSNode(self.game, new_state, self, move)
            self.children.append(child_node)
        self.unexplored_moves = []

    def rollout(self, state, player):
        """
        Perform a rollout (simulation) from the current state.

        Args:
            state: The game state to start the rollout from.
            player: The player for whom the utility is calculated.

        Returns:
            float: The result of the rollout.
        """
        while not self.game.terminal_test(state):
            move = random.choice(state.moves)
            state = self.game.result(state, move)

        value = self.game.utility(state, player)
        return value if value != 0 else 0.5  # Count draw as 0.5

    def backpropagation(self, value):
        """
        Backpropagate the result of the rollout up the tree.

        Args:
            value: The result to propagate.
        """
        node = self
        while node is not None:
            node.visits += 1
            node.wins += value
            node = node.parent

def mcts_player(game, state, iterations=2000):
    """
    Monte Carlo Tree Search algorithm to choose the best move.

    Args:
        game: The game being played.
        state: The current game state.
        iterations: Number of iterations to run the algorithm.

    Returns:
        The best move determined by MCTS.
    """
    player = state.to_move
    root = MCTSNode(game, state)

    for move in state.moves:  # Initialize children
        root.children.append(MCTSNode(game, game.result(state, move), root, move))

    for _ in range(iterations):
        current_node = root

        # Selection
        while current_node.children != []:
            current_node = current_node.selection()

        # Expansion and Rollout
        if game.terminal_test(current_node.state):
            result = game.utility(current_node.state, player)
        else:
            if current_node.visits > 0:
                current_node.expansion()
                current_node = current_node.children[0]
            result = current_node.rollout(current_node.state, player)

        # Backpropagation
        current_node.backpropagation(result)

    # Choose the best move
    best_child = max(root.children, key=lambda child: child.wins / child.visits)
    return best_child.move