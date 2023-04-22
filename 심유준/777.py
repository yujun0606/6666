import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 5, 0.01)
print(x)

def ff(x):
  result = -x ** 2 +6 *x -6
  return result
plt.plot(x, ff(x))
plt.title('functin')
plt.show()