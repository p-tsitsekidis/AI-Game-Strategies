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


game = TicTacToe()

# Testing random player vs minimax player
print("Testing Random Player vs Minimax Player:")
results_minimax = simulate_games(game, randomplayer.random_player, minimax.minimax_player)
print(f"Random Wins: {results_minimax['Player1 Wins']}")
print(f"Minimax Wins: {results_minimax['Player2 Wins']}")
print(f"Draws: {results_minimax['Draws']}")
print(f"Average Decision Time: {results_minimax['Average Time']:.2f} seconds")

# Testing random player vs minimax with pruning
print("\nTesting Random Player vs Minimax with Pruning Player:")
results_minimax_pruning = simulate_games(game, randomplayer.random_player, minimax_pruning.minimax_pruning_player)
print(f"Random Wins: {results_minimax_pruning['Player1 Wins']}")
print(f"Minimax with Pruning Wins: {results_minimax_pruning['Player2 Wins']}")
print(f"Draws: {results_minimax_pruning['Draws']}")
print(f"Average Decision Time: {results_minimax_pruning['Average Time']:.2f} seconds")