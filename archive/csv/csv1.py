import csv

filename = "weather_data.csv"

with open(filename, "r") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)

print("---------------------------")

filename = "weather_data.csv"

with open(filename, "r") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp": temperatures.append(int(row[1]))
        
    print(temperatures)

print("---------------------------")    

