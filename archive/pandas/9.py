import pandas as pd

df = pd.read_csv('data2.csv')

print(df.duplicated())

print('----------------------------------------------')

df = pd.read_csv('data2.csv')
df.drop_duplicates(inplace = True)

print(df.to_string())

print('----------------------------------------------')

df = pd.read_csv('data.csv')

x = df.corr()
print(x)