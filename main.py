from tictactoe import TicTacToe
import randomplayer
import minimax

game = TicTacToe()

utility = game.play_game(randomplayer.random_player, minimax.minimax_player)
if utility == 1:
    print("'X' won!")
elif utility == -1:
    print("'O' won!")
else:
    print('Tie!')