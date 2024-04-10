import matplotlib.pyplot as plt
import numpy as np
print('----------------------------------------------')

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()

print('----------------------------------------------')
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints, marker = 'o')    
plt.show()

print('----------------------------------------------')
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints, 'o')    
plt.show()

print('----------------------------------------------')
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r') # o -> circle, : -> dotted line, r -> red color
plt.show()

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o--r') # -- -> dashed line
plt.show()

print('----------------------------------------------')

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20) #ms -> marker size
plt.show()

print('----------------------------------------------')

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r') #markeredgecolor or the shorter mec to set the color of the edge of the markers
plt.show()

plt.plot(ypoints, 'o:g', ms = 20, mec = 'r') #markeredgecolor or the shorter mec to set the color of the edge of the markers
plt.show()
print('----------------------------------------------')
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()