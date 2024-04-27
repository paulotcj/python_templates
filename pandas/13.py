import pandas as pd
import numpy as np

transactions = pd.read_csv("./transactions.csv")


print(transactions)

print('----------------------------------------------')

print(transactions.shape)

print('----------------------------------------------')
print(f'max index: {transactions.index.max()}')
print('----------------------------------------------')
print('dtypes attribute with column names and their data types')
print(transactions.dtypes)
print('----------------------------------------------')
print('top 5 rows')
print(transactions.head())
print('----')
print('last 5 rows')
print(transactions.tail())

print('----------------------------------------------')
print('get missing counts for all columns')
print(transactions.isna().sum())
print('----------------------------------------------')
print('general info')
print(transactions.info())

print('----------------------------------------------')
print('specified aggregations')
print(transactions.describe())


print('----------------------------------------------')
print('unique dates')
print(transactions['date'].unique())
print('----')
print(f'unique dates count: {transactions["date"].nunique()}')
print('----------------------------------------------')

print(transactions.describe(include="all"))

print('----------------------------------------------')
print('skip the first line and get only store_nbr and transactions columns')
print(transactions.loc[1:,"store_nbr":"transactions"])