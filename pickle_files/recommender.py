# this class gets the similarity of target games against all other games and if greater than 0 stores these in Matrix object.
# [row, col, value] row is the target game id, col is the comparison game id and value is the similarity of the target game to the comparison
class PersonalisedRecommender():

	def __init__(self, cb):
		self.cb = cb
		self.similarities = self.game_similarity_matrix(self.cb)

	def game_similarity_matrix(self, cb):
		sims = Matrix()

		game_ids = list(cb.get_game_ids())

		# can do it this way as Genre Jaccard is symetric, if use different models or adding conditions may need to reconsider.
		for target in range(len(game_ids)):
			for recommendation in range(target+1,len(game_ids)):
				game1 = cb.get_game(game_ids[target])
				game2 = cb.get_game(game_ids[recommendation])
				sim = self.genre_jaccard_similarity(game1, game2)
				if sim > 0:
					sims.add_value(game_ids[target], game_ids[recommendation], sim)
					sims.add_value(game_ids[recommendation], game_ids[target], sim)
		return sims

	# Genre Jaccard similarity
	def genre_jaccard_similarity(self, game1, game2):

		game1_genre_set = set(game1.get_genres())
		game2_genre_set = set(game2.get_genres())

		overlap = game1_genre_set.intersection(game2_genre_set)

		intersection = len(overlap)
		bottom = len(game1.get_genres()) + len(game2.get_genres()) - intersection

		return intersection / bottom

	def get_similarities(self):
		return self.similarities

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