import chess
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
        return self.board.fen()


   


