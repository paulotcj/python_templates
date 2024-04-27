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
print('creating new columns')
transactions["pct_to_target"] = transactions.loc[:, "transaction_count"] / 2500
transactions["met_target"] = transactions.loc[:, "pct_to_target"] >= 1
transactions["bonus_payable"] = 100 * transactions["met_target"]
print(transactions.head())
print('----')
print(transactions.info())
print('Converting a column to a specific data type')
transactions["date"] = transactions["date"].astype("datetime64[ns]")
transactions["month"] = transactions["date"].dt.month
transactions["day_of_week"] = transactions["date"].dt.dayofweek
print(transactions.head())

print('----------------------------------------------')

print('sum on bonus_payable')
print(transactions.loc[:, "bonus_payable"].sum())

print('----------------------------------------------')

# All days in December (month = 12)
# Sundays (day_of_week = 6) in May (month = 5)
# Mondays (day_of_week = 0) in July (month = 7)

conditions = [
    transactions["month"] == 12, # Holiday Bonus
    (transactions["month"] == 5) & (transactions["day_of_week"] == 6), #Corporate Month
    (transactions["month"] == 7) & (transactions["day_of_week"] == 0)  #Summer Special
]
print('conditions')
print(conditions) #conditions is a list containing 3 boolean arrays

print('----')
print('specify outcomes for each condition')
choices = ["Holiday Bonus", "Corporate Month", "Summer Special"]
print(choices)
print('----')

#so in this case we check for true values in the condition list, and map the corresponding choice to the transactions dataframe
# please note that the precedence of the conditions is important, as the first condition that is true will be the one that is chosen
transactions["seasonal_bonus"] = np.select(conditions, choices, default="None")

print(transactions)

print('----------------------------------------------')


print('look at frequency of each bonus type')
print(transactions["seasonal_bonus"].value_counts())

print('----------------------------------------------')
transactions = transactions.drop(
    [
        "pct_to_target",
        "met_target",
        "bonus_payable",
        "month",
        "day_of_week",
        "seasonal_bonus",
    ],
    axis=1,
)

print(transactions.head())

print('----------------------------------------------')



transactions = transactions.assign(
    target_pct = transactions["transaction_count"] / 2500,
    met_target = (transactions["transaction_count"] / 2500) >= 1,
    bonus_payable = ((transactions["transaction_count"] / 2500) >= 1) * 100,
    month = transactions.date.dt.month,
    day_of_week = transactions.date.dt.dayofweek,
    seasonal_bonus = np.select(conditions, choices, default="None"),
)

print(transactions.head())


print('----------------------------------------------')
transactions.info(memory_usage="deep")
print('----')
print('transform the datatype to save memory')
transactions = transactions.astype(
    {
        "store_number": "Int8",
        "transaction_count": "Int16",
        "bonus_payable": "Int8",
        "month": "Int8",
        "day_of_week": "Int8",
        "seasonal_bonus": "category",
    }
)

transactions.info(memory_usage="deep")

print('----------------------------------------------')