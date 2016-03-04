# The chess board is an 8x8 grid
# We'll number the vertical rows
# and alphabetize the horizontal

# Some of the following code was inspired by http://norvig.com/sudoku.html
# Notation in chess is column then row
# Sample Output:
#__|__|__|__|__|__|__|__
#__|__|__|__|__|__|__|__
#__|__|__|__|__|__|__|__
#__|__|__|__|__|__|__|__
#__|__|__|__|__|__|__|__
#__|__|__|__|__|__|__|__
#__|__|__|__|__|__|__|__
#__|__|__|__|__|__|__|__
import gamePiece as gP

class ChessBoard:
	"""docstring for chessBoard"""
	def __init__(self):
		super(ChessBoard, self).__init__()
		self.rows = '12345678'
		self.cols = 'ABCDEFGH'
		self.squares = [col+row for col in self.cols for row in self.rows]

	def printBoard(self, wPlayer, bPlayer):
		units = [['__' for row in self.rows] for col in self.cols]

		for unit in wPlayer:
			units[unit.row-1][unit.col-1] = unit.tag

		for unit in bPlayer:
			units[unit.row-1][unit.col-1] = unit.tag

		for r in range(0,8):
			print('|'.join(str(item) for item in units[r]))

		print('')


# Just testing here
# l = chessBoard()
# l.printBoard()
