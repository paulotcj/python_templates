import pandas

filename = "weather_data.csv"

data = pandas.read_csv(filename)
print("--------------------------------")
print("printing data")
print(data)

print("--------------------------------")
print("printing data[\"temp\"]")
print(data["temp"])

print("--------------------------------")
print("printing types")
print(type(data))
print(type(data["temp"]))

print("--------------------------------")
print("data to dictionary")
data_dict = data.to_dict()
print(data_dict)
print("--------------------------------")
print(data_dict['day'])

temp_list = data['temp'].to_list()

print(temp_list)

print("--------------------------------")

average_temp = sum(temp_list) / len(temp_list)
print(f"the average temperature is: {average_temp}")


print("--------------------------------")
print(f"the average temperature (using data['temp'].mean()) is: {data['temp'].mean()}")

