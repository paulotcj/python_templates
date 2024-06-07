import pandas as pd

df = pd.read_csv('data2.csv')


df["Date_Fixed"] = pd.to_datetime(df["Date"], errors='coerce')

print(df.to_string())


print('----------------------------------------------')

df = pd.read_csv('data2.csv')

df.dropna(subset = ["Date"], inplace = True)
print(df.to_string())