import pandas as pd

employees = pd.DataFrame(
    {"EmpID": [1, 2, 3], "Name": ["Alice", "Bob", "Charlie"], "DeptID": [10, 20, 30]}
)

departments = pd.DataFrame(
    {"DeptID": [10, 20, 40], "DeptName": ["HR", "Engineering", "Marketing"]}
)

# Merging
pd.merge(employees, departments, on="DeptID")  # INNER JOIN
pd.merge(employees, departments, on="DeptID", how="left")  # Left JOIN
pd.merge(employees, departments, on="DeptID", how="right")  # RIGHT JOIN
pd.merge(employees, departments, on="DeptID", how="outer")  # Outer JOIN

# Concatenation

# Vertically
df1 = pd.DataFrame({"Name": ["Alice", "Bob"]})
df2 = pd.DataFrame({"Name": ["Charlie", "David"]})

pd.concat([df1, df2])

# Horizontally
df1 = pd.DataFrame({"ID": [1, 2]})
df2 = pd.DataFrame({"Score": [90, 80]})

pd.concat([df1, df2], axis=1)
