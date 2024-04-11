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


print('----------------------------------------------')



calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)


print('----------------------------------------------')


values = {"day1": [1,2,3], "day2": [4,5,6,], "day3": [7,8,9]}

myvar = pd.Series(values)

print(myvar)
print(myvar[1])
print(myvar['day2'])


print('----------------------------------------------')
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"]) #myvar should be: "day1": 420, "day2": 380
print(myvar)

print('----------------------------------------------')
mydataset = {
  'col_1': [3, 7, 2],
  'col_2' : [4,5,6,]
}
myvar = pd.DataFrame(mydataset)

print(myvar)

print('----------------------------------------------')

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)