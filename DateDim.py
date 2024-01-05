import pandas as pd

df = pd.read_csv(r'C:\Users\JOLO\Desktop\newcleaned.csv')

df['first_air_date'] = pd.to_datetime(df['first_air_date'])


df['first_air_date'] = df['first_air_date'].dt.strftime('%m/%d/%y')

df['first_air_Day'] = pd.to_datetime(df['first_air_date'], format='%m/%d/%y').dt.day
df['first_air_Month'] = pd.to_datetime(df['first_air_date'], format='%m/%d/%y').dt.month
df['first_air_Year'] = pd.to_datetime(df['first_air_date'], format='%m/%d/%y').dt.year
df['first_air_Quarter'] = pd.to_datetime(df['first_air_date'], format='%m/%d/%y').dt.quarter
df['first_air_MonthName'] = pd.to_datetime(df['first_air_date'], format='%m/%d/%y').dt.strftime('%B')  
df['first_air_DayOfWeek'] = pd.to_datetime(df['first_air_date'], format='%m/%d/%y').dt.strftime('%A')  

df['WeekdayInd'] = (pd.to_datetime(df['first_air_date'], format='%m/%d/%y').dt.dayofweek < 5).astype(int) 

# remove dupilcate first-air-datess
df = df.drop_duplicates(subset='first_air_date')

df['date_id'] = range(1, len(df) + 1)

dim_date = df[[
    'date_id',
    'first_air_date', 
    'first_air_Day',
    'first_air_Month',
    'first_air_Year',
    'first_air_Quarter',
    'first_air_MonthName', 
    'first_air_DayOfWeek', 
    'WeekdayInd'
]]

output_file_path = r'C:\Users\JOLO\Desktop\Dim_Date.txt'
dim_date.to_csv(output_file_path, sep=',', index=False)
