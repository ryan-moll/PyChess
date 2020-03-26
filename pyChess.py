from pawn import Pawn

def gameLoop(): 
    board = [["WR","WP",None,None,None,None,"BP","BR"], ["WN","WP",None,None,None,None,"BP","BN"], ["WB","WP",None,None,None,None,"BP","BB"], ["WQ","WP",None,None,None,None,"BP","BQ"], ["WK","WP",None,None,None,None,"BP","BK"], ["WB","WP",None,None,None,None,"BP","BB"], ["WN","WP",None,None,None,None,"BP","BN"], ["WR","WP",None,None,None,None,"BP","BR"]]
    
    BRA = Rook([0,7], 1, board) # Black A file rook
    BNB = Knight([1,7], 1, board) # Black B file knight
    BBC = Bishop([2,7], 1, board) # Black C file bishop
    #BQD = #Queen([3,7], 1, board) # Black D file queen
    #BKE = #King([4,7], 1, board) # Black E file king
    BBF = Bishop([5,7], 1, board) # Black F file bishop
    BNG = Knight([6,7], 1, board) # Black G file knight
    BRH = Rook([7,7], 1, board) # Black H file rook

    BPA = Pawn([0,6], 1, board) # Black A file pawn
    BPB = Pawn([1,6], 1, board) # Black B file pawn
    BPC = Pawn([2,6], 1, board) # Black C file pawn
    BPD = Pawn([3,6], 1, board) # Black D file pawn
    BPE = Pawn([4,6], 1, board) # Black E file pawn
    BPF = Pawn([5,6], 1, board) # Black F file pawn
    BPG = Pawn([6,6], 1, board) # Black G file pawn
    BPH = Pawn([7,6], 1, board) # Black H file pawn

    WPA = Pawn([0,1], 0, board) # White A file pawn
    WPB = Pawn([1,1], 0, board) # White B file pawn
    WPC = Pawn([2,1], 0, board) # White C file pawn
    WPD = Pawn([3,1], 0, board) # White D file pawn
    WPE = Pawn([4,1], 0, board) # White E file pawn
    WPF = Pawn([5,1], 0, board) # White F file pawn
    WPG = Pawn([6,1], 0, board) # White G file pawn
    WPH = Pawn([7,1], 0, board) # White H file pawn

    WRA = Rook([0,0], 0, board) # White A file rook
    WNB = Knight([1,0], 0, board) # White B file knight
    WBC = Bishop([2,0], 0, board) # White C file bishop
    #WQD = #Queen([3,0], 0, board) # White D file queen
    #WKE = #King([4,0], 0, board) # White E file king
    WBF = Bishop([5,0], 0, board) # White F file bishop
    WNG = Knight([6,0], 0, board) # White G file knight
    WRH = Rook([7,0], 0, board) # White H file rook

    printBoard(board)


def printBoard(board):
    print("____A____B____C____D____E____F____G____H__")
    print(" |    |    |    |    |    |    |    |    |")
    print("8| " + str(board[0][7] or '  ') + " | " + str(board[1][7] or '  ') + " | " + str(board[2][7] or '  ') + " | " + str(board[3][7] or '  ') + " | " + str(board[4][7] or '  ') + " | " + str(board[5][7] or '  ') + " | " + str(board[6][7] or '  ') + " | " + str(board[7][7] or '  ') + " |")
    print(" |____|____|____|____|____|____|____|____|")
    print(" |    |    |    |    |    |    |    |    |")
    print("7| " + str(board[0][6] or '  ') + " | " + str(board[1][6] or '  ') + " | " + str(board[2][6] or '  ') + " | " + str(board[3][6] or '  ') + " | " + str(board[4][6] or '  ') + " | " + str(board[5][6] or '  ') + " | " + str(board[6][6] or '  ') + " | " + str(board[7][6] or '  ') + " |")
    print(" |____|____|____|____|____|____|____|____|")
    print(" |    |    |    |    |    |    |    |    |")
    print("6| " + str(board[0][5] or '  ') + " | " + str(board[1][5] or '  ') + " | " + str(board[2][5] or '  ') + " | " + str(board[3][5] or '  ') + " | " + str(board[4][5] or '  ') + " | " + str(board[5][5] or '  ') + " | " + str(board[6][5] or '  ') + " | " + str(board[7][5] or '  ') + " |")
    print(" |____|____|____|____|____|____|____|____|")
    print(" |    |    |    |    |    |    |    |    |")
    print("5| " + str(board[0][4] or '  ') + " | " + str(board[1][4] or '  ') + " | " + str(board[2][4] or '  ') + " | " + str(board[3][4] or '  ') + " | " + str(board[4][4] or '  ') + " | " + str(board[5][4] or '  ') + " | " + str(board[6][4] or '  ') + " | " + str(board[7][4] or '  ') + " |")
    print(" |____|____|____|____|____|____|____|____|")
    print(" |    |    |    |    |    |    |    |    |")
    print("4| " + str(board[0][3] or '  ') + " | " + str(board[1][3] or '  ') + " | " + str(board[2][3] or '  ') + " | " + str(board[3][3] or '  ') + " | " + str(board[4][3] or '  ') + " | " + str(board[5][3] or '  ') + " | " + str(board[6][3] or '  ') + " | " + str(board[7][3] or '  ') + " |")
    print(" |____|____|____|____|____|____|____|____|")
    print(" |    |    |    |    |    |    |    |    |")
    print("3| " + str(board[0][2] or '  ') + " | " + str(board[1][2] or '  ') + " | " + str(board[2][2] or '  ') + " | " + str(board[3][2] or '  ') + " | " + str(board[4][2] or '  ') + " | " + str(board[5][2] or '  ') + " | " + str(board[6][2] or '  ') + " | " + str(board[7][2] or '  ') + " |")
    print(" |____|____|____|____|____|____|____|____|")
    print(" |    |    |    |    |    |    |    |    |")
    print("2| " + str(board[0][1] or '  ') + " | " + str(board[1][1] or '  ') + " | " + str(board[2][1] or '  ') + " | " + str(board[3][1] or '  ') + " | " + str(board[4][1] or '  ') + " | " + str(board[5][1] or '  ') + " | " + str(board[6][1] or '  ') + " | " + str(board[7][1] or '  ') + " |")
    print(" |____|____|____|____|____|____|____|____|")
    print(" |    |    |    |    |    |    |    |    |")
    print("1| " + str(board[0][0] or '  ') + " | " + str(board[1][0] or '  ') + " | " + str(board[2][0] or '  ') + " | " + str(board[3][0] or '  ') + " | " + str(board[4][0] or '  ') + " | " + str(board[5][0] or '  ') + " | " + str(board[6][0] or '  ') + " | " + str(board[7][0] or '  ') + " |")
    print(" |____|____|____|____|____|____|____|____|")


if __name__=="__main__": 
    gameLoop()