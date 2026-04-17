# From Python Lists
import pandas as pd

data = [
    ["Alice", 25],
    ["Bob", 30],
    ["Charlie", 35]
]

df = pd.DataFrame(data, columns=["Name", "Age"])
print(df)

# From Dictionary of Lists
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}

df = pd.DataFrame(data)

# From NumPy Arrays
import numpy as np

arr = np.array([[1, 2], [3, 4]])
df = pd.DataFrame(arr, columns=["A", "B"])

# From Files
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")
df = pd.read_json("data.json")

# From URl
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# Exploratory Data Analysis
df.head()         # First 5 rows
df.tail()         # Last 5 rows
df.info()         # Column info: types, non-nulls
df.describe()     # Stats for numeric columns
df.columns        # List of column names
df.shape          # (rows, columns)