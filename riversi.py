from game import Game
from collections import namedtuple

GameState = namedtuple('GameState', 'to_move, utility, board, moves')

class Riversi(Game):
    
    def __init__(self, h=8, v=8):
        self.h = h
        self.v = v
        moves = []
        self.initial = GameState(to_move='X', utility=0, board={(4,4): 'X', (4,5): 'O', (5,4): 'O', (5,5): 'X'}, moves=moves)
        
    def actions(self, state):
        
        directions = [
                (0, 1), # Right
                (0, -1), # Left
                (-1, 0), # Up
                (1, 0), # Down
                (-1, -1), # Up left
                (-1, 1), # Up right
                (1, -1), # Down left
                (1, 1) # Down right
            ]
        
        valid_moves = []
    
        # Check around every piece on the board
        for position in state.board.keys():
            if state.board[position] == state.to_move:  # Only calculate from player's own pieces
                for vector in directions:
                    valid_move = self.calculate_valid_moves(state, position, vector)
                    if valid_move and valid_move not in valid_moves: # valid_move may return None (If calculate_valid_moves is unsuccessful) and we need to check whether the move already exists in the valid_moves.
                        valid_moves.append(valid_move)

        state.moves = valid_moves  # Update the state with new valid moves
            
                
                
                
    def calculate_valid_moves(self, state, position, vector):
        x, y = position
        v1, v2 = vector
        dx, dy = x + v1, y + v2

        if not (0 <= dx < 8 and 0 <= dy < 8):  # Check if out of bounds (Is an edge position)
            return None

        new_position = (dx, dy)
        opponent = 'O' if state.to_move == 'X' else 'X'

        # Initial check to see if the immediate next spot is an opponent's marker
        if new_position in state.board and state.board[new_position] == opponent:
            # Continue moving in the vector direction until hitting out of bounds or a different piece
            while 0 <= dx < 8 and 0 <= dy < 8:
                dx += v1
                dy += v2
                new_position = (dx, dy)
                if not (0 <= dx < 8 and 0 <= dy < 8):  # Out of bounds check
                    return None
                if new_position not in state.board or state.board[new_position] != opponent:
                    break

            if new_position in state.board and state.board[new_position] == '.':
                return dx, dy

        return None

            

    def result(self, state, move):
        if move not in state.moves:
            return state  # Illegal move has no effect
        board = state.board.copy()
        board[move] = state.to_move
        moves = list(state.moves)
        moves.remove(move)
        return GameState(to_move=('O' if state.to_move == 'X' else 'X'),
                         utility=self.utility(board, move, state.to_move),
                         board=board, moves=moves)
        
    def display(self, state):
        board = state.board
        print('  1 2 3 4 5 6 7 8')
        for x in range(1, self.h + 1):
            print(x, end=' ')
            for y in range(1, self.v + 1):
                print(board.get((x, y), '.'), end=' ')
            print()

    def utility(self, state, player):
        x_count = sum(1 for pos in state.board if state.board[pos] == 'X')
        o_count = sum(1 for pos in state.board if state.board[pos] == 'O')

        if player == 'X':
            return 1 if x_count > o_count else -1 if x_count < o_count else 0
        else:
            return 1 if o_count > x_count else -1 if o_count < x_count else 0



    def terminal_test(self, state):
        """A state is terminal if a player has no moves."""
        return len(state.moves) == 0