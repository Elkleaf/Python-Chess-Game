import gamePiece

class Rook(gamePiece.GamePiece):
    def __init__(self, tag, row, col, color):
        self.tag = tag
        self.row = row
        self.color = color
        self.col = col
        self.tempRow = row
        self.tempCol = col
        self.temp_legal_moves =[]
        self.legal_moves = []
        self.attack_values = 0


    def set_legal_moves(self):
        possible_moves=[]
        #THESE COULD BE TURNED INTO A LOOP (we can do that after though lol)
        #Moving down seven
        for x in range(0, 8):
            possible_moves.append((self.row +x, self.col))

        #Moving up seven
        for x in range(0, 8):
            possible_moves.append((self.row-x, self.col))

        #Moving left seven
        for x in range(0, 8):
            possible_moves.append((self.row , self.col-x))

        #Moving right seven
        for x in range(0, 8):
            possible_moves.append((self.row , self.col + x))
        # Validate Moves
        output_moves = self.validate_moves(possible_moves)

        #sort moves
        output_moves.sort()
        self.legal_moves = output_moves

    def set_temp_legal_moves(self):
        possible_moves=[]
        #THESE COULD BE TURNED INTO A LOOP (we can do that after though lol)
        #Moving down seven
        for x in range(0, 8):
            possible_moves.append((self.tempRow +x, self.tempCol))

        #Moving up seven
        for x in range(0, 8):
            possible_moves.append((self.tempRow-x, self.tempCol))

        #Moving left seven
        for x in range(0, 8):
            possible_moves.append((self.tempRow , self.tempCol-x))

        #Moving right seven
        for x in range(0, 8):
            possible_moves.append((self.tempRow , self.tempCol + x))
        # Validate Moves
        output_moves = self.validate_moves(possible_moves)

        #sort moves
        output_moves.sort()
        self.temp_legal_moves = output_moves


    def validate_moves(self, possible_moves):
        output_moves = possible_moves
        for move in possible_moves[:]:
            #print ('valid moves function: ', move[0])
            if move[0] > 8 or move[1] > 8 or move[0] < 0 or move[1] < 0:
                output_moves.remove(move)
            if move == (self.row, self.col):
                output_moves.remove(move)
        return output_moves


    def move(self, best_move):
        self.row += best_move[1]
        self.col += best_move[0]

    #                   ....
    #                   [-2,0]
    #                   [-1,0]
    #
    # ....  [0,-2] [0,-1]  R   [0,1][0,2] ......
    #
    #                   [1,0]
    #                   [2,0]
