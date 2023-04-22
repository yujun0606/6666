from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000]
gdp = [300, 543, 1075, 2862, 5959, 10000]

plt.plot(years, gdp, color = 'green', marker = 'o')
plt.xlabel('years')
plt.ylabel('gdp')
plt.title('GDP situation')
plt.show()