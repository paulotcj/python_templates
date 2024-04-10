import matplotlib.pyplot as plt
import numpy as np


y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1) # 1 row, 2 columns, 1st plot
plt.plot(y)

y = np.array([11, 22, 42, 42])

plt.subplot(1, 2, 2) # 1 row, 2 columns, 2nd plot
plt.plot(y)

plt.show()

#------------------------------------------------------------



y = np.array([3, 8, 2, 11])

plt.subplot(1, 3, 1) 
plt.plot(y)



y = np.array([11, 22, 33, 44])

plt.subplot(1, 3, 3) 
plt.plot(y)

plt.show()

#------------------------------------------------------------



y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1) # 2 rows, 1 column, 1st plot
plt.plot(y)



y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2) # 2 rows, 1 column, 2nd plot
plt.plot(y)

plt.show()

#------------------------------------------------------------


y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(y)


y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(y)


y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(y)


y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(y)


y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(y)


y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(y)

plt.show()


#------------------------------------------------------------

#plot 1:

y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(y)
plt.title("SALES")

#plot 2:

y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(y)
plt.title("INCOME")

plt.show()


#------------------------------------------------------------

#plot 1:

y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(y)
plt.title("SALES")

#plot 2:

y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()

