import pandas as pd
import numpy as np

df = pd.read_csv('game_dataset_igdb.csv')

# drop duplicate row. As calling api for a number of consoles if game is on both it will appear multiple times in dataset
df = df.drop_duplicates()

# in platforms column remove []' and replace , with |
df['platforms'] = df['platforms'].apply(lambda x: x.replace('[','').replace(']','').replace('\'','').replace(',','|')) 

# in comparisons column remove []' and replace , with |
df['comparisons'] = df['comparisons'].apply(lambda x: x.replace('[','').replace(']','').replace('\'','').replace(',','|')) 

# create new df with games that have genres as wont be able to make recommendations for ones that do not.
# also remove games without an image
df_genre = df[(df['comparisons'] != "") & (df['cover_id'] != 0)].copy()

# if summary is blank is then put in text, summary not available.
df_genre['summary'] = df_genre['summary'].replace(np.nan, 'Sorry, no summary available for this game.', regex=True)

# Save cleaned data frame to a new csv file.
df_genre.to_csv('dataset_igdb.csv', index=False)

# Save cleaned data frame to a new txt file.
df_genre.to_csv('dataset_igdb.txt',index=False,
                      header=None)