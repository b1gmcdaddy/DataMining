import pandas as pd

data = pd.read_csv(r'C:\Users\JOLO\Desktop\newcleaned.csv')

# replace commas w dash
data['genres'] = data['genres'].str.replace(', ', ' - ')

def count_genres(entry):
    return entry.count(' - ') + 1

def extract_primary_genre(entry):
    return entry.split(' - ')[0]

genre_counts = data['genres'].value_counts().reset_index()
genre_counts.columns = ['genres', 'genre_count']

genre_dimension = genre_counts.copy()
genre_dimension['genre_id'] = range(2000, 2000 + len(genre_dimension))
genre_dimension['primary_genre'] = genre_dimension['genres'].apply(extract_primary_genre)
genre_dimension['genre_count'] = genre_dimension['genres'].apply(count_genres)


genre_dimension = genre_dimension[['genre_id', 'genres', 'primary_genre', 'genre_count']]
genre_dimension.to_csv(r'C:\Users\JOLO\Desktop\Dim_Genre.txt', sep=',', index=False)
