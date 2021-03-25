from gamestate import GameState
import os
import chess
import chess.pgn
for pgnfile in os.listdir("training"):
    pgn = open(os.path.join("training", pgnfile))
    while True:
        try:
            subpgn = chess.pgn.read_game(pgn)
            print(subpgn)
        except:
            break


