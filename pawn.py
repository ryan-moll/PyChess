from piece import Piece

class Pawn(Piece):
    def updateMoves(self, board):
        # TODO: Add pawn promotion
        rank = self.position[1]
        file = self.position[0]
        if self.color: # Piece is black
            if not board[file][rank-1]:
                self.availableMoves.append([file,rank-1])
            #TODO: VALIDATE FILE FOR EDGE CASES
            if board[file+1][rank-1] and board[file+1][rank-1][0] is "W":
                self.availableMoves.append([file+1][rank-1])
            if board[file-1][rank-1] and board[file-1][rank-1][0] is "W":
                self.availableMoves.append([file-1][rank-1])
            if rank is 6:
                if not board[file][rank-1] and not board[file][rank-2]:
                    self.availableMoves.append([file,rank-2])
        else: # Piece is white
            if not board[file][rank+1]:
                self.availableMoves.append([file,rank+1])
            #TODO: VALIDATE FILE FOR EDGE CASES
            if board[file+1][rank+1] and board[file+1][rank+1][0] is "B":
                self.availableMoves.append([file+1][rank+1])
            if board[file-1][rank+1] and board[file-1][rank+1][0] is "B":
                self.availableMoves.append([file-1][rank+1])
            if rank is 1:
                if not board[file][rank+1] and not board[file][rank+2]:
                    self.availableMoves.append([file,rank+2])
        return