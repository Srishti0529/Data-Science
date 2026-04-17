import pandas as pd
df = pd.read_csv("data.csv")

# Handeling Missing Values

# To check if value presents in dataframe are null
df.isnull()

# For each column tells the number of null values present
df.isnull().sum()

# Drop the rows having null values
df.dropna()

# Drop columns with null value
df.dropna(axis=1)

# Fill the null values with 0
df.fillna(0)

# Fills with the average value
df["Age"].fillna(df["Age"].mean())

# Fills with previous value
df.fillna(method="ffill")

# Fills with next value
df.fillna(method="bfill")

# Check the duplicate rows
df.duplicated()

# Drop the duplicate rows
df.drop_duplicates()

# STRING FUNCTIONS

# Case conversion
df["Name"].str.lower()

# Checking Presence
df["City"].str.contains("delhi",case=False)

# Splitting
df["Email"].str.split("@")

# Type conversion
df2=df.dropna().copy()
df2["Age"]=df2["Age"].astype(int)

# Apply the function 
def isminor(x):
    return "Adult" if x >= 25 else "Minor"
df2["Age Group"] = df2["Age"].apply(isminor)

# Map the value with new values
gender_map = {"M": "Male", "F": "Female", "O": "Other"}
df2["Gender"] = df2["Gender"].map(gender_map)

# replacement
df2["City"] = df2["City"].replace({"Delhi": "New Delhi", "Mumbai": "New Mumbai"})
