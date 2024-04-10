import pandas as pd

#note some parts of the code below are an exact or partial copy from 
#   https://www.w3schools.com/python/pandas/pandas_getting_started.asp
# any rights to the code below belong to the original author

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

print('----------------------------------------------')

print(pd.__version__)
print('----------------------------------------------')

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
print('----')
print(myvar[0])

print('----------------------------------------------')
pd_series_v = [1, 7, 2]
pd_series_label = ["row_1", "row_2", "row_3"]


myvar = pd.Series(a, index = pd_series_label)

print(myvar)
print('----')
print(myvar["row_2"])