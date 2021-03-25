import chess
class GameState(object):
    def __init__(self):
        self.board = chess.Board()
    
    def value(self):
        return 0
    

    def successors(self):
        return list(self.board.legal_moves)
    
    def print(self):
        pass


   


