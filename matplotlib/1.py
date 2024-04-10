import matplotlib.pyplot as plt
import numpy as np


x_axis = [2,6]
y_axis = [0,250]

plt.plot(x_axis, y_axis)
plt.show()

print('----------------------------------------------')

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()
print('----------------------------------------------')


plt.plot(xpoints, ypoints, '+')
plt.show()

print('----------------------------------------------')
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()
print('----------------------------------------------')

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()

print('----------------------------------------------')

ypoints = np.array([3, 8, 1, 10, 5, 7])
xpoints = np.array([0, 1, 2, 3,  4, 5])

plt.plot(xpoints, ypoints)
plt.show()

