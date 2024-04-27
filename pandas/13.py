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


# print('----------------------------------------------')