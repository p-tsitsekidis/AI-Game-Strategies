class Game:
    """A game is similar to a problem, but it has a utility for each
    state and a terminal test instead of a path cost and a goal
    test. To create a game, subclass this class and implement actions,
    result, utility, and terminal_test. You may override display and
    successors or you can inherit their default methods. You will also
    need to set the .initial attribute to the initial state; this can
    be done in the constructor."""

    def actions(self, state):
        """Return a list of the allowable moves at this point."""
        raise NotImplementedError

    def result(self, state, move):
        """Return the state that results from making a move from a state."""
        raise NotImplementedError

    def utility(self, state, player):
        """Return the value of this final state to player."""
        raise NotImplementedError

    def terminal_test(self, state):
        """Return True if this is a final state for the game."""
        return not self.actions(state)

    def to_move(self, state):
        """Return the player whose move it is in this state."""
        return state.to_move

    def display(self, state):
        """Print or otherwise display the state."""
        print(state)

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    def play_game(self, *players):
        import time
        """Play an n-person, move-alternating game."""
        state = self.initial
        player_move_times = [[], []]
        while True:
            for i, player in enumerate(players):
                # Start timing for the player's move
                start_time = time.time()
                move = player(self, state)
                state = self.result(state, move)
                end_time = time.time()

                # Store the time taken for this move
                move_time = end_time - start_time
                player_move_times[i].append(move_time)

                if self.terminal_test(state):
                    #self.display(state) # Uncomment if you want to display each game
                    
                    # Calculate average time per move for each player
                    avg_player1_time = sum(player_move_times[0]) / len(player_move_times[0]) if player_move_times[0] else 0
                    avg_player2_time = sum(player_move_times[1]) / len(player_move_times[1]) if player_move_times[1] else 0

                    return self.utility(state, self.to_move(self.initial)), avg_player1_time, avg_player2_time