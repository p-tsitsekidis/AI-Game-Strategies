import random

def random_player(game, state):
    """A random player."""
    actions = game.actions(state)
    while True:
        if not actions:
            return None
        random_action = random.choice(actions)
        return random_action