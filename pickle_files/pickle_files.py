from casebase import DatasetReader
from recommender import PersonalisedRecommender
import pickle

# read in game csv file
game_file = 'dataset_igdb.csv'

# create dataset reader object which reads csv and creates casebase.
reader = DatasetReader(game_file)

# get casebase from reader object
cb = reader.get_casebase()
game_ids = cb.get_game_ids()

# create a pickle file called casebase and store the cb object in this file.
filename = 'casebase'
outfile = open(filename,'wb')
pickle.dump(cb,outfile)
outfile.close()

# create a pickle file called game_IDs and store the id list in this file.
filename = 'game_IDs'
outfile = open(filename,'wb')
pickle.dump(game_ids,outfile)
outfile.close()

# create personal recommender object. This creates a similarity matrix object which we store as pickle file.
recommender = PersonalisedRecommender(cb)

# get similarity matrix object
similarities = recommender.get_similarities()

# create a pickle file called casebase and store the cb object in this file.
filename = 'similarity_matrix'
outfile = open(filename,'wb')
pickle.dump(similarities,outfile)
outfile.close()