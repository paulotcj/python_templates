import matplotlib.pyplot as plt
import numpy as np

#note some parts of the code below are an exact or partial copy from 
#   https://www.w3schools.com/python/matplotlib_histograms.asp and
#   https://www.w3schools.com/python/matplotlib_pie_charts.asp
# any rights to the code below belong to the original author

#------------------------------------------------------------
x = np.random.normal(170, 10, 250) #loc, scale, size -> the distribution is centered around 170, 
# the scale of the standard deviation (spread or width) is 10, and the sample size is 250

print(x)

#------------------------------------------------------------

x = np.random.normal(170, 10, 250) #as per the example above

plt.hist(x)
plt.show() 

#------------------------------------------------------------

y = np.array([35, 25, 25, 15]) 

plt.pie(y)
plt.show() 

#------------------------------------------------------------

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 

#------------------------------------------------------------

plt.pie(y, labels = mylabels, startangle = 90) # start the pie chart at 90 degrees
plt.show() 

#------------------------------------------------------------


myexplode = [0.2, 0, 0, 0.4]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 

#------------------------------------------------------------


myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 

#------------------------------------------------------------


mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 


#------------------------------------------------------------




plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 


#------------------------------------------------------------



plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show()