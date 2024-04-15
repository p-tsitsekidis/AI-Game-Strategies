from game import Game
from collections import namedtuple

GameState = namedtuple('GameState', 'to_move, utility, board, moves')

class Riversi(Game):
    
    def __init__(self, h=8, v=8, k=3):
        self.h = h
        self.v = v
        self.k = k
        moves = [(x, y) for x in range(1, h + 1)
                 for y in range(1, v + 1)]
        self.initial = GameState(to_move='X', utility=0, board={(4,4): 'X', (4,5): 'O', (5,4): 'O', (5,5): 'X'}, moves=moves)
        
    def actions(self, state):
        return None

    def result(self, state, move):
        if move not in state.moves:
            return state  # Illegal move has no effect
        board = state.board.copy()
        board[move] = state.to_move
        moves = list(state.moves)
        moves.remove(move)
        return GameState(to_move=('O' if state.to_move == 'X' else 'X'),
                         utility=self.compute_utility(board, move, state.to_move),
                         board=board, moves=moves)
        
    def display(self, state):
        board = state.board
        print("  1 2 3 4 5 6 7 8")
        for x in range(1, self.h + 1):
            print(x, end=' ')
            for y in range(1, self.v + 1):
                print(board.get((x, y), '.'), end=' ')
            print()

    def utility(self, state, player):
        """Return the value of this final state to player."""
        raise NotImplementedError

    def terminal_test(self, state):
        """Return True if this is a final state for the game."""
        return not self.actions(state)