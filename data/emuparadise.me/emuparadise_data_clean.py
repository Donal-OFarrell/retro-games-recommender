import pandas as pd
import csv

df = pd.read_csv('game_dataset_emuparadise.csv')

# remove anything in brackets title column
df['title'] = df['title'].str.replace(r"\s+\(.*\)","")

# remove anything with square brackets in title columns
df['title'] = df['title'].str.replace(r'\[.*?\]','')

# delete any white space before or after title.
df['title'] = df['title'].str.strip()

# remove , in title column
df['title'] = df['title'].apply(lambda x: x.replace(',','')) 

# multiply average rating by rating count to get average if multiple versions of game or on diff consoles.
df['rating X count'] = df['average_rating'] * df['rating_count']

# remove []'" in genres column and replace , with | 
df['genres'] = df['genres'].apply(lambda x: x.replace('[','').replace(']','').replace('\'','').replace(',','|').replace('\"','')) 

# group by title meaning games with the same name from diff consoles merged together.
# console and genres joined as a set. 
df_grouped = df.groupby([df['title'].str.title()]).agg({
    'rating X count': 'sum',
    'rating_count': 'sum',
    'console': lambda x: ','.join(set(x)),
    'genres': lambda x: '|'.join(set(x)),
})

# when consoles are joined replace , with |
df_grouped['console'] = df_grouped['console'].apply(lambda x: x.replace(',','|')) 

# re calculate average rating by dividing rating * count by rating_count. 
# This will ensure game ratings for game on diff consoles/multiple versions is factored in.
df_grouped['average_rating'] = df_grouped['rating X count'] / df_grouped['rating_count'] 

# drop rating * count as no longer needed.
df_grouped.drop(["rating X count"],axis=1,inplace=True)

# create new df with games that have genres as wont be able to make recommendations for ones that do not.
df_genre = df_grouped[df_grouped['genres'] != ""]

# save this new df to csv
df_genre.reset_index().to_csv('dataset_emuparadise.csv', index=False)

# save this new df to txt file and include "" around every cell and also an index for an id.
df_genre.reset_index().to_csv('dataset_emuparadise.txt', quotechar='"',
                      header=None, quoting=csv.QUOTE_ALL)