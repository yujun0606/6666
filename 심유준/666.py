import matplotlib.pyplot as plt
'''plt.title('plotting')
plt.plot([10, 20, 30, 40],[1, 2, 3, 4])
plt.show()'''

'''plt.title('legend')
plt.plot([10, 20, 30, 40],linestyle = '--', label = 'asc')
plt.plot([40, 30, 20, 10], label = 'desc')
plt.legend()
plt.show()'''

plt.title('marker')
plt.plot([10, 20, 30, 40],'.', label = 'circle')
plt.plot([40, 30, 20, 10],'^', label = 'triangle up')
plt.legend()
plt.show()