class Piece:
    def __init__(self, pos, player):
        self.position = pos # List [x,y] where x is the file and y is the rank- e.g. Rook on A1 has position [0,0]
        self.availableMoves = [] # List of positions [[a,b],[c,d],[e,f]] that the piece can move to from its current position
        self.color = player # Binary value to represent the player value 0 = White, 1 = black
        self.updateMoves()


    # def updateMoves(self):
    #     print("Never initialized updateMoves() for child class")
    #     self.availableMoves = ["AH"]
    #     return 0