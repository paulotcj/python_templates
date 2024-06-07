import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
data_frame = pd.DataFrame(data)

print(data_frame) 
print('----')
x = data_frame["calories"]
print(x)
print('----')
x = data_frame.loc[0]
print(x)
print('----')
x = data_frame.loc[[0,1]]
print(x)
print('----')
print('----------------------------------------------')

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

data_frame = pd.DataFrame(data = data, index = ["day1","day2", "day3"])
print(data_frame)
print('----')
x = data_frame.loc["day2"]
print(x)
print('----------------------------------------------')