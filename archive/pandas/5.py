import pandas as pd

df = pd.read_csv('data.csv')

x = df.head(10)

print(x)

print('----------------------------------------------')
print('head')
x = df.head()
print(x)

print('----------------------------------------------')
print('tail')
x = df.tail()
print(x)

print('----------------------------------------------')
print(df.info()) 