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