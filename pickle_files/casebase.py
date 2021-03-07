import csv

# class used to create a game object.
class Game():

	def __init__(self, id, title, slug_title, consoles, genres, cover_id, release_date, average_rating, rating_count):
		self.id = id
		self.title = title
		self.slug_title = slug_title
		self.consoles = consoles
		self.genres = genres
		self.cover_id = cover_id
		self.release_date = release_date
		self.average_rating = average_rating
		self.rating_count = rating_count

	def get_id(self):
		return self.id

	def get_title(self):
		return self.title

	def get_slug_title(self):
		return self.slug_title

	def get_consoles(self):
		return self.consoles

	def get_genres(self):
		return self.genres

	def get_cover_id(self):
		return self.cover_id

	def get_release_date(self):
		return self.release_date

	def get_average_rating(self):
		return self.average_rating

	def get_rating_count(self):
		return self.__rating_count

	# String representation
	def __str__(self):
		return 'ID:' + str(self.id) + ", Title:" + self.title + ", Consoles:" + ", ".join(str(x) for x in self.consoles)

# class used to create a database of game objects
class Casebase():

	def __init__(self):
		self.cb = {}

	def add_game(self, id, game):
		self.cb[id] = game

	def get_game(self, id):
		return self.cb.get(id)

	def get_games(self):
		return self.cb

	def get_game_ids(self):
		return list(self.cb.keys())

	def get_number_games(self):
		return len(self.cb)

# class reads in csv file with game data, creates game object and adds these game objects to the casebase.
class DatasetReader():

	def __init__(self, game_file):
		self.cb = Casebase()
		self.read_casebase(game_file)

	# have extra parameters here ie summary but dont need for game object. Game obhect can be amended to add these if necessary
	def read_casebase(self, game_file):
		with open (game_file,'r', encoding='utf8') as file:
			data = list(csv.reader(file))
			# start at 1 to avoid heading row.
			for x in range(1,len(data)):
				id = data[x][0]
				title = data[x][1]
				slug_title = data[x][2]
				consoles = data[x][3].split('| ')
				game_url = data[x][4]
				genres = data[x][5].split('| ')
				cover_id = data[x][6]
				cover_url = data[x][7]
				cover_height = data[x][8]
				cover_width = data[x][9]
				summary = data[x][10]
				release_date = data[x][11]
				average_rating = data[x][12]
				rating_count = data[x][13]

				# create game object and add to cb
				game_object = Game(id, title, slug_title, consoles, genres, cover_id, release_date, average_rating, rating_count)
				self.cb.add_game(id, game_object)	

	def get_casebase(self):
		return self.cb
