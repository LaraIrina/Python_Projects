   
import pandas
data = pandas.read_csv("weather_data.csv")

# first line of table taken as headers we can filter with 

#converts data frame to dictionary
data_dict = data.to_dict()
print(data_dict)

#works with series (columns) of the data frame
temp_list = data["temp"].to_list()
print(temp_list)

#shorter way to write the calculation of t he max
print(data.temp.max())

#when we add brackets after data we access the row instead of the colums
#access monday row and name it monday
monday = data[data.day == "Monday"]
print(monday.condition)

#create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data = pandas.DataFrame(data_dict)
#create a new csv file into current folder
data.to_csv("new_data.csv")