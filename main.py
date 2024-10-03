from tictactoe import TicTacToe
from reversi import Reversi
from randomplayer import random_player
from manual_player import manual_player
from minimax import minimax_player
from minimax_pruning import minimax_pruning_player
from minimax_limited_pruning import minimax_limited_pruning_player
from mcts import mcts_player

def simulate_games(game, player1, player2, num_games):
    results = {
        'Player1_Wins': 0,
        'Player2_Wins': 0,
        'Draws': 0,
        'Average_Player1_Move_Time': 0,
        'Average_Player2_Move_Time': 0
        }
    
    total_player1_move_time = 0
    total_player2_move_time = 0
    
    for _ in range(num_games):
        utility, avg_player1_time, avg_player2_time = game.play_game(player1, player2)
        
        total_player1_move_time += avg_player1_time
        total_player2_move_time += avg_player2_time
        
        if utility == 1:
            results['Player1_Wins'] += 1
        elif utility == -1:
            results['Player2_Wins'] += 1
        else:
            results['Draws'] += 1
    
    results['Average_Player1_Move_Time'] = total_player1_move_time / num_games
    results['Average_Player2_Move_Time'] = total_player2_move_time / num_games
    return results

def game_initialization(game, player_1, player_2, num_of_games):
    print("\n\nThe game is starting:")
    results = simulate_games(game, player_1, player_2, num_of_games)
    print(f"Player 1 Wins: {results['Player1_Wins']}")
    print(f"Player 2 Wins: {results['Player2_Wins']}")
    print(f"Draws: {results['Draws']}")
    print(f"Average Player 1 Move Time: {results['Average_Player1_Move_Time']:.4f} seconds")
    print(f"Average Player 2 Move Time: {results['Average_Player2_Move_Time']:.4f} seconds")

all_players = {
    1: manual_player,
    2: random_player,
    3: minimax_player,
    4: minimax_pruning_player,
    5: minimax_limited_pruning_player,
    6: mcts_player
}

games = {
    "1": TicTacToe(),
    "2": Reversi()
}

print("Choose which game you would like to play:")
print("1. Tic Tac Toe")
print("2. Reversi (Othello)")

while True:
    game_choice = input("Enter your choice: ")
    if game_choice == "1" or game_choice == "2":
        break
    else:
        print("Invalid input. Please enter either '1' or '2'.")

game = games.get(game_choice)

for i in range(2):
    print(f"\n\nChoose Player {i+1}:")
    print("1. Human Player (You)")
    print("2. Random Player")
    print("3. Minimax Player")
    print("4. Minimax with Pruning Player")
    print("5. Minimax with Limited Pruning Player")
    print("6. Monte Carlo Player")

    while True:
        try:
            player_choice = int(input("Enter your choice: "))
            if 1 <= player_choice <= 6:
                break
            else:
                print("Invalid input. Please enter a single number that corresponds to your choice.")
        except ValueError:
            print("Invalid input. Please enter a single number that corresponds to your choice.")

    if i == 0:
        player_1 = all_players.get(player_choice)
    else:
        player_2 = all_players.get(player_choice)

print("Enter the number of games you wish to play (Statistics are shown at the end)")
while True:
    try:
        num_of_games = int(input("Enter a positive integer: "))
        if num_of_games > 0:
            break
        else:
            print("Invalid number. Please enter a positive integer that reflects the number of games you wish to play.")
    except ValueError:
        print("Invalid input. Please enter a positive integer that reflects the number of games you wish to play.")

game_initialization(game, player_1, player_2, num_of_games)