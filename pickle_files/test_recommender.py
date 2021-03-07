import pickle

# get recommendations based on target games and pickle files
# uses target_games, similarites and cb global variables defined below. 
def get_recommendations():

	recommendations = {}
	game_ids = cb.get_game_ids()

	for game_id in game_ids:
		if game_id not in target_games:
			mean_relevance = 0
			for target_id in target_games:
				score = similarities.get_value(target_id, game_id)
				mean_relevance += score
			if mean_relevance > 0:
				recommendations[game_id] = mean_relevance / len(target_games)

	return recommendations

# read in casebase pickle file and store as var cb
filename = 'casebase'
infile = open(filename,'rb')
cb = pickle.load(infile)
infile.close()

# read in matrix pickle file and store as var similarities
filename = 'similarity_matrix'
infile = open(filename,'rb')
similarities = pickle.load(infile)
infile.close()

# set target list of game to test but this will be received from front end in the future. This is game id's which can be gotten from 'dataset_igdb.csv'
target_games = ['11219','3327','1187','7431']

# print list of target games
print('Target Games:')
for game in target_games:
	print(cb.get_game(game).get_title())
print()

# call get recommendations function
recs = get_recommendations()

# print recommendations of list of target games.
num_recs = 10
if len(recs) > 0 :
	print('Recommended Games:')
	count = 0
	# this sorts dictionary by highest value meaning best rates games first in dict.
	for key,value in sorted(recs.items(), key=lambda x: x[1], reverse=True):
		if count < num_recs and count < len(recs):
			print(cb.get_game(key).get_title() +'. Similarity:'+ str(round(recs[key], 2)))
			count += 1