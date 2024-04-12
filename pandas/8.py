import pandas as pd

df = pd.read_csv('data2.csv')

df.loc[7, 'Duration'] = 45
print(df.to_string())

print('----------------------------------------------')

df = pd.read_csv('data2.csv')

for i, v in df.iterrows():
    print(f'i: {i}, v[\"Duration\"]: {v["Duration"]}')
    
    
print('----------------------------------------------')

df = pd.read_csv('data2.csv')
for x in df.index:
    if df.loc[x, "Duration"] >= 121:
        df.loc[x, "Duration"] = 120
        
print(df.to_string())

print('----------------------------------------------')

df = pd.read_csv('data2.csv')
for x in df.index:
    if df.loc[x, "Duration"] >= 121:
        df.drop(x, inplace = True)
        
print(df.to_string())


    


 
 