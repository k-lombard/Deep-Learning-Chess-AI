from gamestate import GameState
import os
import chess
import chess.pgn
import numpy as np
def parse():
    games = []
    values = []
    for pgnfile in os.listdir("training"):
        pgn = open(os.path.join("training", pgnfile))
        while True:
            try:
                subpgn = chess.pgn.read_game(pgn)
                #print(subpgn)
            except:
                break

            value_assign_dict = {'1-0': 1, '0-1': -1, '1/2-1/2':0} 
            #Assigns game results to values; a win for white is 1, a win for black is -1, a draw is 0.
            try:
                game_value = value_assign_dict[subpgn.headers['Result']]
            except:
                break
            #not going to include draws for more efficient learning; we will ommit game values of 0.
            #print(game_value)

            tempboard = subpgn.board()
            #Pushes all moves of the subpgn onto the board
            for move in subpgn.mainline_moves():
               
                
                tempboard.push(move)
                output = GameState(tempboard).print()
                games.append(output)
                values.append(game_value)
                
                
            
            print(games, values)









