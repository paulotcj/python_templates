import pandas as pd

data_frame = pd.read_csv('data.csv')

new_data_frame = data_frame.dropna() #method provided by pandas that is used to remove missing values (NaN) from the DataFrame. By default, it removes any row in which at least one null value is present.
print(new_data_frame.to_string())
print('----')
print(f'data_frame info: {data_frame.info()}') #169 entries
print('----')
print(f'new_data_frame info: {new_data_frame.info()}') #164 entries

print('----------------------------------------------')

data_frame = pd.read_csv('data.csv')
print(f'data_frame info: {data_frame.info()}') #169 entries
data_frame.dropna(inplace = True)
print(f'data_frame info: {data_frame.info()}') #164 entries

print('----------------------------------------------')