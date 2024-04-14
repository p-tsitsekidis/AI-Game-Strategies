import numpy as np

def minimax_pruning_player(game, state):
    """Given a state in a game, calculate the best move by searching
    forward all the way to the terminal states."""
    
    a = -np.inf
    b = np.inf
    
    player = game.to_move(state)

    def max_value(state, a, b):
        if game.terminal_test(state):
            return game.utility(state, player)

        v = -np.inf
        for action in game.actions(state):
            v = max(v, min_value(game.result(state, action), a, b))
            if (v >= b):
                return v
            a = max(a,v)
        return v

    def min_value(state, a, b):
        if game.terminal_test(state):
            return game.utility(state, player)

        v = np.inf
        for action in game.actions(state):
            v = min(v, max_value(game.result(state, action), a, b))
            if v <= a:
                return v
            b = min(b, v)
        return v

    return max(game.actions(state), key=lambda action: min_value(game.result(state, action), a, b))