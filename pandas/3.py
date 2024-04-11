import pandas as pd

data_frame = pd.read_csv('data.csv')

x = data_frame.to_string()
print(x)
print('----')
print(data_frame)

print('----------------------------------------------')

print(pd.options.display.max_rows)

print('----------------------------------------------')

pd.options.display.max_rows = 10_000
data_frame = pd.read_csv('data.csv')
print(data_frame)

print('----')

pd.options.display.max_rows = 10
data_frame = pd.read_csv('data.csv')
print(data_frame)
pd.options.display.max_rows = 60
print('----------------------------------------------')