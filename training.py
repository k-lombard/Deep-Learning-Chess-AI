import random
from gamestate import GameState
import os
import chess
import chess.pgn
import numpy as np
import csv

def parse():
    games = []
    values = []
    for pgnfile in os.listdir("games"):
        pgn = open(os.path.join("games", pgnfile))
        count = 0
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
            count += 1
            print("parsing game number " + str(count))
            for move in subpgn.mainline_moves():


                tempboard.push(move)
                output = GameState(tempboard).bit_encode()
                games.append(output)
                values.append(game_value)


    games = np.array(games)
    values = np.array(values)
    return games, values
    #print(games, values)


def prepare_data():

    positions = []
    results = []
    x = 0

    for pgnfile in os.listdir("games"):
        pgn = open(os.path.join("games", pgnfile))
        value_assign_dict = {'1-0': [1,0], '0-1': [0,1], '1/2-1/2': [0,0]}

        while (True):
            try:
                subpgn = chess.pgn.read_game(pgn)
            except:
                break

            try:
                game_value = value_assign_dict[subpgn.headers['Result']]
            except:
                break

            if game_value[0] == 0 and game_value[1] == 0:
                continue

            upper_bound = subpgn.end().ply()

            if upper_bound <= 5:
                continue

            tempboard = subpgn.board()
            mainline_moves = subpgn.mainline_moves()

            for j in range(10):
                tempboard.reset()
                move_number = random.randint(5, upper_bound)
                iterator = iter(mainline_moves)
                for i in range(move_number):
                    tempboard.push(next(iterator))
                trian_game_value = game_value[0]
                positions.append(GameState(tempboard).bit_encode())
                results.append(trian_game_value)
                x+=1

    positions = np.array(positions)
    results = np.array(results)
    np.save('./data/positions.npy', positions)
    np.save('./data/results.npy', results)
    print(x)

