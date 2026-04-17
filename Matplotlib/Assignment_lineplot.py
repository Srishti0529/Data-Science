#Question
#"Plot a line graph using Matplotlib to
# compare the yearly runs of Virat Kohli,
# Rohit Sharma, and MS Dhoni from 2009 to 2019. 
# Use different colors and line styles for each player, add legend, title, and axis labels."


import matplotlib.pyplot as plt

kohli = [325, 995, 1381, 1026, 1268, 1054, 623, 739, 1460, 1202, 1377]
rohit = [301, 598, 691, 284, 1537, 1015, 1269, 1349, 1793, 1804, 2442]
dhoni = [443, 600, 764, 524, 753, 418, 640, 278, 371, 275, 204]

years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

plt.style.use("ggplot")

plt.plot(years , kohli , color="red", linestyle="-." , label="Virat Kohli")
plt.plot(years , rohit , color="blue", linestyle="--" , label="Rohit Sharma")
plt.plot(years , dhoni , color="green", linestyle=":" , label="Mahendra Singh Dhoni")

plt.legend()

plt.title("Comparison of runs")
plt.xlabel("Year")
plt.ylabel("Runs")

plt.show()