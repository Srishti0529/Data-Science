# Series — 1D Labeled Array
import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)

# You can also define custom index:
s = pd.Series([10, 20, 30], index=["a", "b", "c"])

# A DataFrame is like a dictionary of Series — multiple columns with labels.
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["Delhi", "Mumbai", "Bangalore"]
}

df = pd.DataFrame(data)
print(df)