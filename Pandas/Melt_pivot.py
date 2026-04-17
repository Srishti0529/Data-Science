import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 78, 92],
    'Science': [90, 82, 89],
    'English': [88, 85, 94]
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)


# MELT 
df.melt(id_vars=["Name"], value_vars=["Math", "Science", "English"], var_name="Subject", value_name="Score")
# id_vars=["Name"]: We keep the "Name" column as it is because it's the identifier.
# value_vars=["Math", "Science", "English"]: These are the columns we want to melt.
# var_name="Subject": The new column containing the names of the subjects.
# value_name="Score": The new column containing the scores.

# PIVOT
df.pivot(index=None, columns=None, values=None)
# index="Name": The unique values in the "Name" column will become the rows in the new DataFrame.
# columns="Subject": The unique values in the "Subject" column will become the columns in the new DataFrame.
# values="Score": The values from the "Score" column will populate the table.