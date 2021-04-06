import chess
import numpy as np

class GameState(object):
    def __init__(self, board=None):
        if board==None:
            self.board = chess.Board()
        else:
            self.board = board

    def value(self):
        return 0


    def successors(self):
        return list(self.board.legal_moves)

    def bit_encode(self):
        #encodes a board state as a 774 "bitstring" which is an array of 1s or 0s.
        #6 pieces * 64 squares * 2 colors = 768 + 6 bits for castling/to-move/en passant = 774 bits
        bitstring = []
        for num in range(64):

            if self.board.piece_at(num) == None:
                empty = [0,0,0,0,0,0,0,0,0,0,0,0]
                bitstring = bitstring + empty
                continue
            bit_map = {"P": [1,0,0,0,0,0,0,0,0,0,0,0], "N": [0,1,0,0,0,0,0,0,0,0,0,0], "B": [0,0,1,0,0,0,0,0,0,0,0,0], "R": [0,0,0,1,0,0,0,0,0,0,0,0], "Q": [0,0,0,0,1,0,0,0,0,0,0,0], "K": [0,0,0,0,0,1,0,0,0,0,0,0], "p": [0,0,0,0,0,0,1,0,0,0,0,0], "n":[0,0,0,0,0,0,0,1,0,0,0,0], "b":[0,0,0,0,0,0,0,0,1,0,0,0], "r":[0,0,0,0,0,0,0,0,0,1,0,0], "q":[0,0,0,0,0,0,0,0,0,0,1,0], "k": [0,0,0,0,0,0,0,0,0,0,0,1]}
            temp = self.board.piece_at(num)
            type_of_piece = temp.symbol()
            piece = bit_map[type_of_piece]
            bitstring = bitstring + piece
            continue

        if self.board.has_queenside_castling_rights(chess.WHITE):
            bitstring.append(1)
        else:
            bitstring.append(0)

        if self.board.has_kingside_castling_rights(chess.WHITE):
            bitstring.append(1)
        else:
            bitstring.append(0)
        if self.board.has_queenside_castling_rights(chess.BLACK):
            bitstring.append(1)
        else:
            bitstring.append(0)
        if self.board.has_kingside_castling_rights(chess.BLACK):
            bitstring.append(1)
        else:
            bitstring.append(0)

        if self.board.has_legal_en_passant():
            bitstring.append(1)
        else:
            bitstring.append(0)
        if self.board.turn == chess.WHITE:
            bitstring.append(1)
        else:
            bitstring.append(0)





        return bitstring





