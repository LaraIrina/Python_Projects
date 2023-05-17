   
import pandas
# data = pandas.read_csv("weather_data.csv")

# # first line of table taken as headers we can filter with 

# #converts data frame to dictionary
# data_dict = data.to_dict()
# print(data_dict)

# #works with series (columns) of the data frame
# temp_list = data["temp"].to_list()
# print(temp_list)

# #shorter way to write the calculation of t he max
# print(data.temp.max())

# #when we add brackets after data we access the row instead of the colums
# #access monday row and name it monday
# monday = data[data.day == "Monday"]
# print(monday.condition)

# #create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# new_data = pandas.DataFrame(data_dict)
# #create a new csv file into current folder
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrel_count = len(gray_squirrels)

cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_squirrel_count = len(cinnamon_squirrels)

black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrel_count = len(black_squirrels)

data_dict = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [gray_squirrel_count,cinnamon_squirrel_count,black_squirrel_count]
}

new_data_frame = pandas.DataFrame(data_dict)
new_data_frame.to_csv("squirrel_color_count.csv")