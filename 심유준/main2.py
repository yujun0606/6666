import seaborn as sns
from matplotlib import pyplot as plt
iris = sns.load_dataset('iris')
print(iris.head(10))
print(iris['species'])
plt.scatter(iris.sepal_length, iris.sepal_width)
plt.show()