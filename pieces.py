from piece import Piece 

class King(Piece):
    def updateMoves(self, board):
        rank = self.position[1]
        file = self.position[0]

        if rank+1 <=7:
            if rank+1 <= 7 and not board[file][rank+1]:
                self.availableMoves.append([file+i, rank])
            elif board[file][rank+1] and board[file][rank+1][0] is 

class Queen(Piece):
    def updateMoves(self, board):
        rank = self.position[1]
        file = self.position[0]

        i = 1  #this gives the queen the ability to move forwards, backwards, side to side
        while file+i <= 7:
            if not board[file+i][rank]:
                self.availableMoves.append([file+i, rank])
            elif not self.color and board[file+i][rank][0] is "B":
                self.availableMoves.append([file+i, rank])
            elif self.color and board[file+i][rank][0] is "W":
                self.availableMoves.append([file+i, rank])
            else break:
        
        while file-i >= 0:
            if not board[file+i][rank]:
                self.availableMoves.append([file-i, rank])
            elif not self.color and board[file-i][rank][0] is "B":
                self.availableMoves.append([file-i, rank])
            elif self.color and board[file-i][rank][0] is "W":
                self.availableMoves.append([file-i, rank])
            else break:

        while rank+i <= 7:
            if not board[file][rank+i]:
                self.availableMoves.append([file, rank+i])
            elif not self.color and board[file][rank+i][0] is "B":
                self.availableMoves.append([file, rank+i])
            elif self.color and board[file][rank+i][0] is "W":
                self.availableMoves.append([file, rank+i])
            else break:
        while rank-i >= 0:
            if not board[file][rank+i]:
                self.availableMoves.append([file, rank+i])
            elif not self.color and board[file][rank+i][0] is "B":
                self.availableMoves.append([file, rank+i])
            elif self.color and board[file][rank+i][0] is "W":
                self.availableMoves.append([file, rank+i])
            else break:

        i = 1 # This gives the queen the ability move diagonally
        while file+i <=7 and rank+i <= 7:
           if not board[file+i][rank+i]:
                self.availableMoves.append([file+i, rank+i])
            elif not self.color and board[file+i][rank+i][0] is "B":
                self.availableMoves.append([file+i, rank+i])
            elif self.color and board[file+i][rank+i][0] is "W":
                self.availableMoves.append([file+i, rank+i])
            else break: 

         while file-i >= 0 and rank+i <= 7:
           if not board[file-i][rank+i]:
                self.availableMoves.append([file-i, rank+i])
            elif not self.color and board[file-i][rank+i][0] is "B":
                self.availableMoves.append([file-i, rank+i])
            elif self.color and board[file-i][rank+i][0] is "W":
                self.availableMoves.append([file-i, rank+i])
            else break: 

         while file+i <=7 and rank-i >= 0:
           if not board[file+i][rank-i]:
                self.availableMoves.append([file+i, rank-i])
            elif not self.color and board[file+i][rank-i][0] is "B":
                self.availableMoves.append([file+i, rank-i])
            elif self.color and board[file+i][rank-i][0] is "W":
                self.availableMoves.append([file+i, rank-i])
            else break:  

        while file-i >= 0 and rank-i >= 0:
           if not board[file+i][rank-i]:
                self.availableMoves.append([file-i, rank-i])
            elif not self.color and board[file-i][rank-i][0] is "B":
                self.availableMoves.append([file-i, rank-i])
            elif self.color and board[file-i][rank-i][0] is "W":
                self.availableMoves.append([file-i, rank-i])
            else:
                break
        return





class Bishop(Piece):
    def updateMoves(self, board):
        rank = self.position[1]
        file = self.position[0]

        i = 1
        while file+i <=7 and rank+i <= 7:
           if not board[file+i][rank+i]:
                self.availableMoves.append([file+i, rank+i])
            elif not self.color and board[file+i][rank+i][0] is "B":
                self.availableMoves.append([file+i, rank+i])
            elif self.color and board[file+i][rank+i][0] is "W":
                self.availableMoves.append([file+i, rank+i])
            else break: 

         while file-i >= 0 and rank+i <= 7:
           if not board[file-i][rank+i]:
                self.availableMoves.append([file-i, rank+i])
            elif not self.color and board[file-i][rank+i][0] is "B":
                self.availableMoves.append([file-i, rank+i])
            elif self.color and board[file-i][rank+i][0] is "W":
                self.availableMoves.append([file-i, rank+i])
            else break: 

         while file+i <=7 and rank-i >= 0:
           if not board[file+i][rank-i]:
                self.availableMoves.append([file+i, rank-i])
            elif not self.color and board[file+i][rank-i][0] is "B":
                self.availableMoves.append([file+i, rank-i])
            elif self.color and board[file+i][rank-i][0] is "W":
                self.availableMoves.append([file+i, rank-i])
            else break:  

        while file-i >= 0 and rank-i >= 0:
           if not board[file+i][rank-i]:
                self.availableMoves.append([file-i, rank-i])
            elif not self.color and board[file-i][rank-i][0] is "B":
                self.availableMoves.append([file-i, rank-i])
            elif self.color and board[file-i][rank-i][0] is "W":
                self.availableMoves.append([file-i, rank-i])
            else:
                break

        return

class Knight(Piece):
    def updateMoves(self, board):
        rank = self.position[1]
        file = self.position[0]

        if not board[file+1][rank+2]:
            self.availableMoves.append([file+1, rank+2])
        elif self.color and board[file+1][rank+2][0] is "W":
            self.availableMoves.append([file+1, rank+2])

         if not board[file+1][rank-2]:
            self.availableMoves.append([file+1, rank-2])
        elif self.color and board[file+1][rank-2][0] is "W":
            self.availableMoves.append([file+1, rank-2])

         if not board[file-1][rank+2]:
            self.availableMoves.append([file-1, rank+2])
        elif self.color and board[file-1][rank+2][0] is "W":
            self.availableMoves.append([file-1, rank+2])

         if not board[file-1][rank-2]:
            self.availableMoves.append([file-1, rank-2])
        elif self.color and board[file-1][rank-2][0] is "W":
            self.availableMoves.append([file-1, rank-2])

         if not board[file+2][rank+1]:
            self.availableMoves.append([file+2, rank+1])
        elif self.color and board[file+2][rank+1][0] is "W":
            self.availableMoves.append([file+2, rank+1])

         if not board[file+2][rank-1]:
            self.availableMoves.append([file+2, rank-1])
        elif self.color and board[file+2][rank-1][0] is "W":
            self.availableMoves.append([file+2, rank-1])

         if not board[file-2][rank+1]:
            self.availableMoves.append([file-2, rank+1])
        elif self.color and board[file-2][rank+1][0] is "W":
            self.availableMoves.append([file-2, rank+1])

         if not board[file-2][rank-1]:
            self.availableMoves.append([file-2, rank-1])
        elif self.color and board[file-2][rank-1][0] is "W":
            self.availableMoves.append([file-2, rank-1]) 


        return


class Rook(Piece):
    def updateMoves(self, board):
        rank = self.position[1]
        file = self.position[0]

        i = 1 
        while file+i <= 7:
            if not board[file+i][rank]:
                self.availableMoves.append([file+i, rank])
            elif not self.color and board[file+i][rank][0] is "B":
                self.availableMoves.append([file+i, rank])
            elif self.color and board[file+i][rank][0] is "W":
                self.availableMoves.append([file+i, rank])
            else break:
        
        while file-i >= 0:
            if not board[file+i][rank]:
                self.availableMoves.append([file-i, rank])
            elif not self.color and board[file-i][rank][0] is "B":
                self.availableMoves.append([file-i, rank])
            elif self.color and board[file-i][rank][0] is "W":
                self.availableMoves.append([file-i, rank])
            else break:

        while rank+i <= 7:
            if not board[file][rank+i]:
                self.availableMoves.append([file, rank+i])
            elif not self.color and board[file][rank+i][0] is "B":
                self.availableMoves.append([file, rank+i])
            elif self.color and board[file][rank+i][0] is "W":
                self.availableMoves.append([file, rank+i])
            else break:
        while rank-i >= 0:
            if not board[file][rank+i]:
                self.availableMoves.append([file, rank+i])
            elif not self.color and board[file][rank+i][0] is "B":
                self.availableMoves.append([file, rank+i])
            elif self.color and board[file][rank+i][0] is "W":
                self.availableMoves.append([file, rank+i])
            else break:
        return

class Pawn(Piece):
    def updateMoves(self, board):
        # TODO: Add pawn promotion
        rank = self.position[1]
        file = self.position[0]
        if self.color: # Piece is black
            if not board[file][rank-1] and rank-1 >= 0:
                self.availableMoves.append([file,rank-1])
            #TODO: VALIDATE FILE FOR EDGE CASES
            if file+1 <= 7 and rank-1 >=0 and board[file+1][rank-1] and board[file+1][rank-1][0] is "W":
                self.availableMoves.append([file+1][rank-1])
            if file-1 >=0 and rank-1 >= 0 and board[file-1][rank-1] and board[file-1][rank-1][0] is "W":
                self.availableMoves.append([file-1][rank-1])
            if rank is 6:
                if not board[file][rank-1] and not board[file][rank-2]:
                    self.availableMoves.append([file,rank-2])
        else: # Piece is white
            if not board[file][rank+1]:
                self.availableMoves.append([file,rank+1])
            #TODO: VALIDATE FILE FOR EDGE CASES
            if file+1 <= 7 and rank+1 <= 7 and board[file+1][rank+1] and board[file+1][rank+1][0] is "B":
                self.availableMoves.append([file+1][rank+1])
            if file-1 >= 0 and rank+1 <= 7 and board[file-1][rank+1] and board[file-1][rank+1][0] is "B":
                self.availableMoves.append([file-1][rank+1])
            if rank is 1:
                if not board[file][rank+1] and not board[file][rank+2]:
                    self.availableMoves.append([file,rank+2])
        return