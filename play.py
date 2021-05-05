#alpha beta pruning
from keras.models import Model, load_model
import keras
import chess
import copy
import numpy as np
from gamestate import GameState
import tensorflow as tf
import chess.pgn

supervised_path = "./network/DeepLearningModel.h5"
model = load_model(supervised_path)

board = chess.Board()


board2 = chess.Board()

board.push_san("e4")
board.push_san("e5")
board.push_san("Qh5")
board.push_san("Nf6")
board.push_san("a3")
board.push_san("Nxh5")
board.push_san("b3")

board2.push_san("e3")
board2.push_san("e5")
board2.push_san("Nf3")
board2.push_san("e4")
board2.push_san("a3")
board2.push_san("exf3")
board2.push_san("b4")

movemap = {}

def alpha_beta_search(alpha_pos, beta_pos, curr, max_depth, white):
    if max_depth == 0:
        return curr
    
    if white == True:
        first = False
        for move in curr.legal_moves:
            new_node = copy.deepcopy(curr)
            new_node.push(move)
            if first == False:
                leaf = alpha_beta_search(alpha_pos, beta_pos, new_node, max_depth-1, False)
                first = True
            if alpha_pos == -1:
                alpha_pos = leaf
            second = alpha_beta_search(alpha_pos, beta_pos, new_node, max_depth-1, False)
            output = prediction(leaf, second)
            try:
                output = output.numpy()
            except:
                pass
            if output[0][0] > output[0][1]:
                better = leaf
            else:
                better = second
            output2 = prediction(alpha_pos, better)
            try:
                output2 = output2.numpy()
            except:
                pass
            if output2[0][0] > output2[0][1]:
                pass
            else:
                alpha_pos = better
            if beta_pos != 1:
                final = prediction(alpha_pos, beta_pos)
                try:
                    final = final.numpy()
                except:
                    pass
                if final[0][0] > final[0][1]:
                    break
        return better
            
    else:
        first = False
        for move in curr.legal_moves:
            new_node = copy.deepcopy(curr)
            new_node.push(move)
            if first == False:
                leaf = alpha_beta_search(alpha_pos, beta_pos, new_node, max_depth-1, True)
                first = True
            if beta_pos == 1:
                beta_pos = leaf
            second = alpha_beta_search(alpha_pos, beta_pos, new_node, max_depth-1, True)
            output = prediction(leaf, second)
            try:
                output = output.numpy()
            except:
                pass
            if (output[0][1]) > (output[0][0]):
                better = second
            else:
                better = leaf
            output2 = prediction(beta_pos, better)
            try:
                output2 = output2.numpy()
            except:
                pass
            if (output2[0][1]) > (output2[0][0]):
                beta_pos = better
            else:
                pass
            if alpha_pos != -1:
                final = prediction(alpha_pos, beta_pos)
                try:
                    final = final.numpy()
                except:
                    pass
                if (final[0][0]) > (final[0][1]):
                    break
        return better



def prediction(pos1, pos2):
    global model
    global movemap
    if pos1.fen() in movemap and pos2.fen() in movemap:
        return np.array([[movemap[pos1.fen()], movemap[pos2.fen()]], []])
    else:
        new1 = np.array(GameState(pos1).bit_encode())[np.newaxis]
        new2 = np.array(GameState(pos2).bit_encode())[np.newaxis]
        pos = [[new1],[new2]]

        output = model(pos)
        temp = output.numpy()
        movemap[pos1.fen()] = temp[0][0]
        movemap[pos2.fen()] = temp[0][1]
        return output
        #tf.Tensor([[0.14621536 0.8537846 ]], shape=(1, 2), dtype=float32)




def computer(board, depth):
    alpha = -1
    beta = 1
    first = False
    for move in board.legal_moves:
        new_node = copy.deepcopy(board)
        new_node.push(move)
        if first == False:
            output = alpha_beta_search(alpha, beta, new_node, depth-1, False)
            best = move
            if alpha == -1:
                alpha = output
            first = True
        else:
            temp = alpha_beta_search(alpha, beta, new_node, depth-1, False)
            new_output = prediction(temp, output)
            try:
                new_output = new_output.numpy()
            except:
                pass
            if (new_output[0][0]) > (new_output[0][1]):
                new_output2 = temp
            else:
                new_output2 = output
            if new_output2 != output:
                best = move
                output = new_output2
            alpha = prediction(alpha, output)
           
            try:
                alpha = alpha.numpy()
            except:
                pass
            if (alpha[0][0]) > (alpha[0][1]):
                pass
            else:
                alpha = output
    print(best)	
    board.push(best)
    
    return board

def player(board):
	while 1==1:
		try:
			move = input("Enter player move: \n")
			board.push_san(move)
			break
		except ValueError:
			print("Illegal move; please enter a new move:")

	return board

def play():
    moveNum = 0
    board = chess.Board()
    depth = input("Enter max search depth \n")
    depth = int(depth)
    
    while 1==1:
        if board.is_game_over() == True:
            break
        print(board)
        if moveNum % 2 == 0:
            board = computer(board, depth) #computer is white
        else:
            board = player(board)
        moveNum += 1
    print(board)
    print("Game over.")
    
    game = chess.pgn.Game.from_board(board)
    print(game)


play()
