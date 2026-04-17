import matplotlib.pyplot as plt

# VERTICAL BAR CHARTS

# Single Labelling
years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
runs =  [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]

plt.bar(years, runs)
plt.xlabel("Year")
plt.ylabel("Runs Scored")
plt.title("Sachin Tendulkar's Yearly Runs")
plt.show()

# Multiple Labelling
import numpy as np

sachin = [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
sehwag = [0, 200, 900, 1400, 1600, 1800, 1500, 1100, 800, 0]
kohli  = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]

x = np.arange(len(years))  # index positions
width = 0.25
plt.bar(x - width, sachin, width=width, label="Sachin")
plt.bar(x, sehwag, width=width, label="Sehwag")
plt.bar(x + width, kohli, width=width, label="Kohli")

plt.xlabel("Year")
plt.ylabel("Runs")
plt.title("Run Comparison")
plt.xticks(x, years)  # Show actual year instead of 0,1,2,...
plt.legend()
plt.tight_layout()
# is used to automatically adjust spacing between plot elements so that labels, titles, and legends do not overlap or get cut off.
plt.show()


# Horizonatal Bar Charts
players = ["Sachin", "Sehwag", "Kohli", "Yuvraj"]
runs_5yrs = [500+700+1100+1500+1800, 0+200+900+1400+1600, 0+0+500+800+1100, 300+600+800+1100+900]
plt.barh(players, runs_5yrs, color="skyblue")
plt.xlabel("Total Runs in First 5 Years")
plt.title("First 5-Year Performance of Indian Batsmen")
plt.tight_layout()
plt.show()

# Adding Values
import matplotlib.pyplot as plt

players = ["Sachin", "Sehwag", "Kohli"]
runs = [1500, 1200, 1800]

plt.bar(players, runs, color="skyblue")

# Add labels on top of bars
for i in range(len(players)):
    plt.text(i, runs[i] + 50, str(runs[i]), ha='center')

# for i in range(len(players)):
# Loops through each player index one by one.

# i
# Represents the x-axis position of the current player.

# runs[i]
# Gets the run value of the current player.

# runs[i] + 50
# Positions the text slightly above the bar/point to avoid overlap.

# str(runs[i])
# Converts the run value to text so it can be displayed.

# plt.text(i, runs[i] + 50, str(runs[i]), ha='center')
# Writes the run value as centered text on the plot above each bar or point.

plt.ylabel("Runs")
plt.title("Runs Scored by Players")
plt.tight_layout()
plt.show()