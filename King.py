import gamePiece

class King(gamePiece.GamePiece):

    def __init__(self, tag, row, col, color):
        self.tag = tag
        self.color = color
        self.row = row
        self.col = col
        self.tempRow = row
        self.tempCol= col
        self.temp_legal_moves =[]
        self.legal_moves = []
        self.attack_value = 0

    def set_legal_moves(self):
        possibleMoves = []
		
		# Append list of all offsets
        possibleMoves.append((self.row - 1, self.col))
        possibleMoves.append((self.row, self.col - 1))
        possibleMoves.append((self.row - 1, self.col - 1))
        possibleMoves.append((self.row + 1, self.col - 1))
        possibleMoves.append((self.row - 1, self.col + 1))
        possibleMoves.append((self.row + 1, self.col))
        possibleMoves.append((self.row, self.col + 1))
        possibleMoves.append((self.row + 1, self.col + 1))
        # Validate Moves
        outputMoves = self.validate_moves(possibleMoves)

        # Sort Moves
        outputMoves.sort()
        self.legal_moves = outputMoves

    def set_temp_legal_moves(self):
        possibleMoves = []

		# Append list of all offsets
        possibleMoves.append((self.tempRow - 1, self.tempCol))
        possibleMoves.append((self.tempRow, self.tempCol - 1))
        possibleMoves.append((self.tempRow - 1, self.tempCol - 1))
        possibleMoves.append((self.tempRow + 1, self.tempCol - 1))
        possibleMoves.append((self.tempRow - 1, self.tempCol + 1))
        possibleMoves.append((self.tempRow + 1, self.tempCol))
        possibleMoves.append((self.tempRow, self.tempCol + 1))
        possibleMoves.append((self.tempRow + 1, self.tempCol + 1))
        # Validate Moves
        outputMoves = self.validate_moves(possibleMoves)

        # Sort Moves
        outputMoves.sort()
        self.temp_legal_moves = outputMoves

    def validate_moves(self, possibleMoves):
        outputMoves = possibleMoves

        for move in possibleMoves[:]:
            if move[0] > 8 or move[1] > 8 or move[0] <= 0 or move[1] <= 0:
                outputMoves.remove(move)
            if move == (self.row, self.col):
                outputMoves.remove(move)
        return outputMoves


    # def check_for_others(self, possible_moves, other_piece):
    #     output_moves = possible_moves
    #     for move in possible_moves:
    #         if (move[0] == other_piece.row) and (move[1] == other_piece.col):
    #             output_moves.remove(move)
    #
    #     return output_moves

    def current_position(self):
        return [self.row, self.column]

