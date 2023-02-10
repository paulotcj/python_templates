import pandas

filename = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"


data = pandas.read_csv(filename)

grey_squirrels_count = len( data[ data["Primary Fur Color"] == "Gray" ] )
red_squirrels_count = len( data[ data["Primary Fur Color"] == "Cinnamon" ] )
black_squirrels_count = len( data[ data["Primary Fur Color"] == "Black" ] )

print(f"Counts - Grey:{grey_squirrels_count}, Red:{red_squirrels_count}, Black:{black_squirrels_count}")

data_dict = {
    "Fur Color" : ["Gray","Cinnamon","Black"],
    "Count" : [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)

df.to_csv("squirrel_count.csv")