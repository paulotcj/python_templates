import pandas as pd
import numpy as np

transactions = pd.read_csv("./transactions.csv")


print(transactions)

print('----------------------------------------------')

print(transactions.shape)

print('----------------------------------------------')
print(f'max index: {transactions.index.max()}')
print('----------------------------------------------')
print('dtypes attribute with column names and their data types')
print(transactions.dtypes)
print('----------------------------------------------')
print('top 5 rows')
print(transactions.head())
print('----')
print('last 5 rows')
print(transactions.tail())

print('----------------------------------------------')
print('get missing counts for all columns')
print(transactions.isna().sum())
print('----------------------------------------------')
print('general info')
print(transactions.info())

print('----------------------------------------------')
print('specified aggregations')
print(transactions.describe())


print('----------------------------------------------')
print('unique dates')
print(transactions['date'].unique())
print('----')
print(f'unique dates count: {transactions["date"].nunique()}')
print('----------------------------------------------')

print(transactions.describe(include="all"))

print('----------------------------------------------')
print('skip the first line and get only store_nbr and transactions columns')
print(transactions.loc[1:,"store_nbr":"transactions"])

print('----------------------------------------------')

print(transactions.loc[:, "store_nbr"].nunique())


print('----------------------------------------------')
print('drop the first row of data in place')
transactions.drop(0, axis=0, inplace=True)
print(transactions)

print('----------------------------------------------')
print('drop date but not in place')
print(transactions.drop("date", axis=1))
print('----')
print(transactions)

print('----------------------------------------------')
print('drop duplicate rows subsetting by store number. keep last entry for each store')

print(transactions.drop_duplicates(subset="store_nbr", keep="last").head())

print('----------------------------------------------')

oil = pd.read_csv("./oil.csv")

print(oil)
print('----')
print(oil.info())
print('----')
print(oil.isna().sum())

print('----------------------------------------------')
print('calculate mean of oil series after filling missing values with 0')
print(oil.loc[:, 'dcoilwtico'].fillna(0).mean().round(2))


print('calculate mean of oil series after filling missing values with the mean of oil price')

print(
        oil.loc[:, 'dcoilwtico'].fillna(
            oil.loc[:, 'dcoilwtico'].mean()
        ).mean().round(2)
    )

print('----------------------------------------------')
print('all stores > 2500 percentage occurence')

print( (transactions['transactions'] > 2000).mean() )

print('----------------------------------------------')
print('Number of times store 25 had > 2000 divided by total days for store 25 to get percent of time it happened')

mask = (transactions['transactions'] > 2000) & (transactions['store_nbr'] == 25)

x = (transactions.loc[mask, 'transactions'].count() 
 / transactions.loc[(transactions['store_nbr'] == 25), 'transactions'].count())
print(x)

print('----------------------------------------------')
print('Sum of transactions where store 25 had > 2000 transactions')
print(transactions.loc[mask, 'transactions'].sum())

print('----------------------------------------------')
print('sum of transactions for stores 25 and 31 in months May and June on days they had less than 2000 transactions')
x = (transactions.query(
    "store_nbr in [25, 31] & date.str[6] in ['5', '6'] & transactions < 2000")
    .loc[:, "transactions"]
    .sum())
print(x)


print('----------------------------------------------')
print('Sort dataframe by date in ascending order, and trasactions in descending order')

x = transactions.sort_values(['date', 'transactions'], ascending=[True, False])
print(x)

print('----------------------------------------------')
print('sort columns')
x = transactions.sort_index(axis=1, ascending=False)
print(x)
print('----')
x = transactions.sort_index(axis=1, ascending=True)
print(x)

print('----------------------------------------------')

print('rename columns and reindex where axis=1 reorders the columns')
print(transactions.head())
print('----')
x = transactions =(transactions
 .rename(
    columns={"transactions": "transaction_count", "store_nbr": "store_number"})
 .reindex(labels=["date", "transaction_count", "store_number"], axis=1)
)

print(x.head())

print('----------------------------------------------')




# print('----------------------------------------------')

