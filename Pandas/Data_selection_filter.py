import pandas as pd

# Selection
df = pd.read_csv("movies.csv")
print(df)

# To print specific columns
df[['Actor', 'IMDb']]

# Label Based 
df.loc[1] 
df.loc[7, 'IMDb']
df.loc[0:2, ["Actor", "IMDb", "Film"]]
# It is slicing last number inclusive

# Index based
df.iloc[1]
df.iloc[7, 5]
df.iloc[0:2, 0:2]
# It is slicing last number exclusive

# Fast Access
df.at[0, "Actor"] 
# By column name
df.iat[0, 0]
# By column number


# Filtering
df[df['IMDb']>6]

# Using query
df.query("Year > 2018 and IMDb >6")