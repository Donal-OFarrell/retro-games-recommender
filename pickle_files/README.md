casebase.py contains 3 classes. 
Game - this class creates the game object
Casebase - this class creates a database of game objects.
DatasetReader - this class reads in 'dataset_igdb.csv' and creates games objects from the data and adds these game objects to the casebase.

recommender.py contains two classes.
PersonalisedRecommender - this class creates the similarities matrix which is a dictionary containing dictionaries (row, col, value). row is the target game id, col is the comparison game id and value is the similarity of the target game to the comparison.The similarity metric used is the Genre Jaccard. 
Matrix - this is a class to create the similarities matrix object (dictionary of dictionaries) along with methods to add and get values from this.

pickle_files.py - run this script and two pickle files will output. 'casebase' which is the database of game objects and 'similarity_matrix' which is described in detail in the class above.

test_recommender.py - On line 34 there is a list of target games which can be edited to test the accuracy of the recommender. The value needed is the game id which can be gotten from 'dataset_igdb.csv'. This then reads in the pickle files generated, calls a get_recommendations function which uses the mean similarity of target games to comparisons to get recommendations for the overall target list of games.  