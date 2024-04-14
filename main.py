from tictactoe import TicTacToe
import randomplayer
import minimax
import minimax_pruning
import time

def simulate_games(game, player1, player2, num_games=100):
    results = {'Player1 Wins': 0, 'Player2 Wins': 0, 'Draws': 0, 'Average Time': 0}
    total_time = 0
    
    for _ in range(num_games):
        start_time = time.time()
        utility = game.play_game(player1, player2)
        end_time = time.time()
        
        total_time += (end_time - start_time)
        
        if utility == 1:
            results['Player1 Wins'] += 1
        elif utility == -1:
            results['Player2 Wins'] += 1
        else:
            results['Draws'] += 1
    
    results['Average Time'] = total_time / num_games
    return results
