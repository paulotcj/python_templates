import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

sns.distplot([0, 1, 2, 3, 4, 5])
# sns.displot([0, 1, 2, 3, 4, 5], kde=True)
# sns.displot([0, 1, 2, 3, 4, 5])

plt.show()

print('----------------------------------------------')
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()


x = random.normal(size=(2, 3))

print(x)

print('----------------------------------------------')
sns.distplot(random.normal(size=1000), hist=False)

plt.show()