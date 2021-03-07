# this class creates the Matrix object used to hold game similarities.
class Matrix():

	def __init__(self):
		self.matrix = {}

	def add_value(self, row, col, value):
		if row in self.matrix:
			map = self.matrix[row]
		else:
			map = {}
		map[col] = value
		self.matrix[row] = map

	def get_value(self, row, col):
		if (row in self.matrix and col in self.matrix[row]):
			return self.matrix[row][col]
		else:
			return 0