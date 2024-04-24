import pandas as pd
import numpy as np

oil = pd.read_csv("./oil.csv").dropna()


oil_array = np.array(oil["dcoilwtico"].iloc[1000:1100])

print(oil_array)
print('----------------------------------------------')
oil_series = pd.Series(oil_array, name="oil_prices")
print(oil_series)

print('----------------------------------------------')
print(f"Name: {oil_series.name}")
print(f"dtype: {oil_series.dtype}")
print(f"size: {oil_series.size}")
print(f"index: {oil_series.index}")

print('----------------------------------------------')
print(f'oil series mean value: {oil_series.values.mean()}')

print(f'oil series (int) mean value: {oil_series.astype("int").values.mean()}')
print('----------------------------------------------')
dates = pd.Series(oil["date"]).iloc[1000:1100]
print('Dates:')
print(dates)
print('----------------------------------------------')
print(oil_series)
print('----')
oil_series.index = dates
print(oil_series)
print('----')
print(oil_series.iloc[:10])

print('----------------------------------------------')
print('Mean of first 10 prices')
print(oil_series.iloc[:10].mean())

print('----------------------------------------------')
print('Mean of last 10 prices')

print(oil_series.iloc[-10:].mean())

print('----------------------------------------------')
print('Slice labels using loc, reset index and drop dates to return series w/ integer index')

print(oil_series.loc["2017-01-01":"2017-01-07"].reset_index(drop=True))

print('----------------------------------------------')
print('Get 10 lowest prices by grabbing first 10 rows of sorted price series\nThen, sort by index in descending order')
print(oil_series.sort_values().iloc[:10].sort_index(ascending=False))

print('----------------------------------------------')


print('Create mask to filter to only dates in list of dates and oil price <= 50')
dates = [
    "2016-12-22",
    "2017-05-03",
    "2017-01-06",
    "2017-03-05",
    "2017-02-12",
    "2017-03-21",
    "2017-04-14",
    "2017-04-15",
]

mask = oil_series.index.isin(dates) & (oil_series <= 50)
print('Mask:')
print(mask)
print('----')
print('oil series filtered by mask:')
print(oil_series.loc[mask])


print('----------------------------------------------')
print(oil_series)
print('----')
print(oil_series * 1.1 + 2)
print('----')
print(oil_series)
print('----------------------------------------------')

max_price = oil_series.max()

max_price

print(f'Max price: {max_price}')

print('----------------------------------------------')
print((oil_series - max_price) / max_price)

print('----------------------------------------------')
string_dates = pd.Series(oil_series.index)
print('Dates:')
print(string_dates)
print('----------------------------------------------')
print(string_dates.str[5:7].astype("int"))
print('----------------------------------------------')

print(pd.Series(oil_series.index).str[5:7].astype("int"))
print('----------------------------------------------')


print('Filter series to March (month 3), calculate sum of prices, and round')

print(oil_series[oil_series.index.str[6:7] == "3"].sum().round(2))

print('----------------------------------------------')
print('Filter series to march, calculate mean')

print(oil_series[oil_series.index.str[6:7] == "3"].mean())
print(oil_series[oil_series.index.str[6:7] == "3"].mean().round(2))

print('----------------------------------------------')
print('Filter series to Jan and Feb, count entries')

print(oil_series[oil_series.index.str[6:7].isin(["1", "2"])].count())

print('----------------------------------------------')
print('Calculate 10th and 90th percentiles of oil series using quantile')
print(oil_series.quantile([0.1, 0.9]))

print('----------------------------------------------')
print('Return normalized value counts to get percentage of time each integer dollar value occurred')
print(oil_series.astype("int").value_counts(normalize=True))

print('----------------------------------------------')
print('Fill in two values with missing data')
print(oil_series)
print('----')
oil_series = oil_series.where(~oil_series.isin([51.44, 47.83]), pd.NA)
print(oil_series)