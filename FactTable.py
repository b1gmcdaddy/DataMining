import pandas as pd

data = pd.read_csv(r'C:\Users\JOLO\Desktop\newcleaned.csv')

data['first_air_date'] = pd.to_datetime(data['first_air_date'])
data['first_air_date'] = data['first_air_date'].dt.strftime('%m/%d/%y')
data['genres'] = data['genres'].str.replace(', ', ' - ')
data['popularity'] = data['popularity'].round(2)

#selected cols
fact_table = data[[
    'show_name', 
    'genres', 
    'original_language', 
    'first_air_date', 
    'popularity', 
    'number_of_seasons', 
    'number_of_episodes'
]].copy()

fact_table.to_csv(r'C:\Users\JOLO\Desktop\FactTable.txt', sep=',', index=False)
