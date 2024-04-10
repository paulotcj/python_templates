import matplotlib.pyplot as plt
import numpy as np

#note some parts of the code below are an exact or partial copy from 
#   https://www.w3schools.com/python/matplotlib_scatter.asp
# any rights to the code below belong to the original author

x = np.array([4,8,7,7,2,17,2,10,4,12,12,13,7])
y = np.array([100,86,85,88,110,86,100,87,90,78,80,85,81])

plt.scatter(x, y)
plt.show()

#------------------------------------------------------------

#day one measurements
x = np.array([4,8,7,7,2,17,2,10,4,12,12,13,7])
y = np.array([100,86,85,88,110,86,100,87,90,78,80,85,81])
plt.scatter(x, y)

#day 2 measurements
x = np.array([2,2,8,1,10,8,12,9,7,3,11,4,7,14,12])
y = np.array([105,110,84,105,95,105,95,100,94,105,79,112,91,80,85])
plt.scatter(x, y)

plt.show()

#------------------------------------------------------------


x = np.array([4,8,7,7,2,17,2,10,4,12,12,13,7])
y = np.array([100,86,85,88,110,86,100,87,90,78,80,85,81])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,10,8,12,9,7,3,11,4,7,14,12])
y = np.array([105,110,84,105,95,105,95,100,94,105,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()

#------------------------------------------------------------

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()

#------------------------------------------------------------

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.show()

#------------------------------------------------------------

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()


#------------------------------------------------------------

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes)

plt.show()


#------------------------------------------------------------

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()

#------------------------------------------------------------

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()