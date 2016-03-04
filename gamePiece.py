class GamePiece(object):
	"""docstring for GamePiece"""
	def __init__(self, tag, row, col):
		super(GamePiece, self).__init__()
		self.tag = tag
		self.row = row
		self.col = col
		