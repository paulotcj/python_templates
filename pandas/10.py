import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()

print('----------------------------------------------')

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()


print('----------------------------------------------')
df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show()

print('----------------------------------------------')

df = pd.read_csv('data.csv')

df["Duration"].plot(kind = 'hist')
plt.show()