class Piece:
    def __init__(self, pos, player):
        self.position = pos
        self.availableMoves = []
        self.color = player
        self.updateMoves()


    def updateMoves(self):
        print("Never initialized updateMoves() for child class")
        self.availableMoves = ["AH"]
        return 0