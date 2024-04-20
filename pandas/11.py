import pandas as pd


numbers_array = [2,4,6,8,10]
numbers_labels = ['two','four','six','eight','ten']

pd_series = pd.Series(numbers_array)

print(pd_series)
print('----')
print(pd_series[0])
print('----')
print(pd_series.iloc[1:3]) #based on indexes, will return indexes from 1 to 2 (3 not included)
print('----')
#based on labels, it will consider the index numbers as labels
# and will return from 1 to 3 (3 included)
print(pd_series.loc[1:3])


print('----------------------------------------------')


numbers_array = [2,4,6,8,10]
numbers_labels = ['a','b','a','c','a']
pd_series = pd.Series(numbers_array, index=numbers_labels)
print(pd_series)
print('----')
print(pd_series['a'])

print('----------------------------------------------')

numbers_array = [2,4,6,8,10]
numbers_labels = ['a','b','a','c','a']
pd_series = pd.Series(numbers_array, index=numbers_labels)
print(pd_series)
print('----')
pd_series.reset_index(drop=True, inplace=True)
print(pd_series)


print('----------------------------------------------')

numbers_array = [2,4,6,8,10]
numbers_labels = ['a','b','a','c','a']
pd_series = pd.Series(numbers_array, index=numbers_labels)

x = pd_series.index.isin(["test", "a", "c"])
print(x)


print('----------------------------------------------')

numbers_array = [2,4,6,8,10]
numbers_labels = ['a','b','a','c','a']
pd_series = pd.Series(numbers_array, index=numbers_labels)

x = None
pd_series.sort_values(inplace=True)
print(pd_series)
print('----')
pd_series.sort_values(ascending=False, inplace=True)
print(pd_series)
print('----')

pd_series.sort_index(inplace=True)
print(pd_series)
print('----')

pd_series.sort_index(ascending=False, inplace=True)
print(pd_series)
print('----')
