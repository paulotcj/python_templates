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


print('----------------------------------------------')


sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

plt.show()


sns.distplot(random.binomial(n=1, p=0.5, size=1000), hist=True, kde=False)

plt.show()

print('----------------------------------------------')
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()

print('----------------------------------------------')

x = random.poisson(lam=2, size=10)

print(x)
print('----------------------------------------------')
sns.distplot(random.poisson(lam=2, size=1000), kde=False)

plt.show()

print('----------------------------------------------')
sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')

plt.show()