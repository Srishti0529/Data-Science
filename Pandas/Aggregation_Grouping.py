import pandas as pd
df = pd.DataFrame({
    "Department": ["HR", "HR", "IT", "IT", "Marketing", "Marketing", "Sales", "Sales"],
    "Team": ["A", "A", "B", "B", "C", "C", "D", "D"],
    "Gender": ["M", "F", "M", "F", "M", "F", "M", "F"],
    "Salary": [85, 90, 78, 85, 92, 88, 75, 80],
    "Age": [23, 25, 30, 22, 28, 26, 21, 27],
    "JoinDate": pd.to_datetime([
        "2020-01-10", "2020-02-15", "2021-03-20", "2021-04-10",
        "2020-05-30", "2020-06-25", "2021-07-15", "2021-08-01"
    ])
})  

df.groupby("Department")["Salary"].mean()
# “Group by Department, then calculate average Salary for each group.”

# Aggregation Functions
df.groupby("Team")["Salary"].mean()     # Average per team
df.groupby("Team")["Salary"].sum()      # Total score
df.groupby("Team")["Salary"].count()    # How many entries
df.groupby("Team")["Salary"].min()
df.groupby("Team")["Salary"].max()

# Custon Aggregation
df.groupby("Team")["Salary"].agg(
    avg_score="mean",
    high_score="max"
)

# Now each row gets its team average
df["Team Avg"] = df.groupby("Team")["Salary"].transform("mean")

# Only keeps teams with average score > 80.
df.groupby("Team").filter(lambda x: x["Salary"].mean() > 80)