#Question
#"Create a horizontal bar chart using Matplotlib to 
#display the total runs scored by Sachin Tendulkar, 
#Virat Kohli, and Virender Sehwag in their first 5 years. 
#Also display the run values on each bar and add appropriate labels and title."

import matplotlib.pyplot as plt

players = ["Sachin Tendulkar", "Virat Kohli", "Virender Sehwag"]
debut_5yr_runs = [3200, 2600, 2900]

plt.barh(players, debut_5yr_runs)

# Add text labels on bars
for i in range(len(players)):
    plt.text(debut_5yr_runs[i] + 25, i, str(debut_5yr_runs[i]), va='center')

plt.xlabel("Runs")
plt.ylabel("Players")
plt.title("Total Runs in First 5 Years")
plt.tight_layout()
plt.show()
