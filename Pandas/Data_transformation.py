import pandas as pd
df = pd.read_csv("data.csv")

# Sorting
df.sort_values("Year",'IMDb')

# Arrange the index in ascending order after sorting
df2 = df.sort_values("Year").copy()
df2.reset_index()
# Actual data df2 does not change

# creates a new column and give rank according to highest imdb rating and gives integer value only for same rating as well
df2["Rank"] = df2["IMDb"].rank(ascending=False, method="dense") 

# Change the order of columns
df = df[["Film", "Actor", "Year", "Genre", "IMDb", "BoxOffice(INR Crore)"]] 

# Tojust change first coming and remaining same
cols = ["Name"] + [col for col in df.columns if col != "Name"]
df = df[cols]

# Renaming 
df.rename(columns={"Year": "Releasing"}, inplace=True)
# inplace=True → changes the DataFrame directly (no need to store it in another variable)
