import random

def random_player(game, state):
    """A random player."""
    game.display(state)
    actions = game.actions(state)
    while True:
        random_action = random.choice(actions)
        print(random_action)
        return random_action