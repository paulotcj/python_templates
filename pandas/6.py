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

df = pd.read_csv('data.csv')
df.fillna(9_999_999, inplace = True) #replace all NaN values with 9,99,999
print(df.to_string())


print('----------------------------------------------')

df = pd.read_csv('data.csv')
# df["Calories"].fillna(9_999_999, inplace = True) #replace all NaN values in the "Calories" column with 9,99,999 #deprecated

df.fillna({"Calories": 11_111_111}, inplace=True)
print(df.to_string())

print('----------------------------------------------')

df = pd.read_csv('data.csv')
x = df["Calories"].mean()
print(x)
print('----')
df.fillna({"Calories": x}, inplace = True)
print(df.to_string())

print('----------------------------------------------')
#median -> sorting the values and finding the middle value
df = pd.read_csv('data.csv')
x = df["Calories"].median()
print(x)
df.fillna({"Calories": x}, inplace = True)
print(df.to_string())

print('----------------------------------------------')
#mode -> the values that appear most frequently
df = pd.read_csv('data.csv')
x = df["Calories"].mode() # return a series, so we will have: [0, value] -> [0, 300]
print(type(x)) 
print(x) #0    300
print(x[0]) #300

print('----')
df.fillna({"Calories": x[0]}, inplace = True)
print(df.to_string())






