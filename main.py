from tictactoe import TicTacToe
import randomplayer
import minimax

game = TicTacToe()

minimax_counter = 0
random_counter = 0
draw_counter = 0

for _ in range(100):
    utility = game.play_game(randomplayer.random_player, minimax.minimax_player)
    if utility == 1:
        random_counter += 1
    elif utility == -1:
        minimax_counter += 1
    else:
        draw_counter += 1
        
print(random_counter)
print(minimax_counter)
print(draw_counter)