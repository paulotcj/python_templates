import matplotlib.pyplot as plt
import numpy as np

#note some parts of the code below are an exact or partial copy from 
#   https://www.w3schools.com/python/matplotlib_bars.asp
# any rights to the code below belong to the original author

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()


#------------------------------------------------------------

x = np.array(["APPLES", "BANANAS"])
y = np.array([400, 350])
plt.bar(x, y)
plt.show()


#------------------------------------------------------------

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y) #horizontal bars
plt.show()


#------------------------------------------------------------

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()


#------------------------------------------------------------

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "hotpink")
plt.show()

#------------------------------------------------------------

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()

#------------------------------------------------------------


x = np.array(["A", "B", "C", "DDD"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, height = 0.5 ) #for horizontal bars the height means the thickness
# so therefore you cannot set the width of the bars here
plt.show()