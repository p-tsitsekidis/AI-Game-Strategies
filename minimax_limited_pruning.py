import numpy as np
from reversi import Reversi

def minimax_limited_pruning_player(game, state):
    """Given a state in a game, calculate the best move by searching
    forward limited to a depth of 3."""
    
    a = -np.inf
    b = np.inf
    initial_depth = 0
    
    reversi_game = Reversi()
    
    player = game.to_move(state)

    def max_value(state, a, b, current_depth):     
        if game.terminal_test(state):
            return game.utility(state, player)
        if current_depth == 3:
            return reversi_game.evaluateHeuristicFunction(state)

        v = -np.inf
        for action in game.actions(state):
            v = max(v, min_value(game.result(state, action), a, b, current_depth + 1))
            if (v >= b):
                return v
            a = max(a,v)
        return v

    def min_value(state, a, b, current_depth):
        if game.terminal_test(state):
            return game.utility(state, player)
        if current_depth == 3:
            return reversi_game.evaluateHeuristicFunction(state)

        v = np.inf
        for action in game.actions(state):
            v = min(v, max_value(game.result(state, action), a, b, current_depth + 1))
            if v <= a:
                return v
            b = min(b, v)
        return v

    return max(game.actions(state), key=lambda action: min_value(game.result(state, action), a, b, initial_depth))