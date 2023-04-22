import seaborn as sns
from matplotlib import pyplot as plt
iris = sns.load_dataset('iris')
groups = iris.groupby('species') # 종류별로 그룹화
fig, ax = plt.subplots()
for name, group in groups:
  ax.scatter(group.sepal_length, group.sepal_width, label = name)
ax.legend(loc='upper right')#범례
plt.show()
