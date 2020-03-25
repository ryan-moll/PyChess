from piece import Piece

class Pawn(Piece):
    def updateMoves(self):
        print("I AM PAWN AH")
        self.availableMoves = ["PAWN MOVEZ"]
        return 0
