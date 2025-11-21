# with open("weather_data.csv") as weather_deets:
#     for each_day in weather_deets:
#         weekly_weather = weather_deets.readlines()
#         print(weekly_weather)
#
# import csv
#
# with open("weather_data.csv", "r", newline='') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #get Data in Columns
# print(data['condition'])
# print(data.condition)
#
# #get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp)
#
# monday_farh = monday.temp[0]
# monday_temp_f = monday_farh * 9/5 + 32
#
# print(monday_temp_f)
#
# #Create a dataframe from scratch
# data_dict = {
#     "students": ['bob', 'tae', 'jacquelyn'],
#     "scores": [88, 91, 75]
# }
#
# data_score = pandas.DataFrame(data_dict)
# data.to_csv("Student_Scores.csv")
#
# average = sum(temp_list) / len(temp_list)
#
# print(data)
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))
#
# dict_weather = data.to_dict()
# temp_dict = data["temp"].to_dict()
# print(dict_weather)





import pandas

squirrels = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251121.csv")

gray_data = len(squirrels[squirrels['Primary Fur Color'] == "Gray"])
red_data = len(squirrels[squirrels['Primary Fur Color'] == "Cinnamon"])
black_data = len(squirrels[squirrels['Primary Fur Color'] == "Black"])
print(gray_data)
print(red_data)
print(black_data)

data_dict = {
    "Fur color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [gray_data, red_data, black_data]
}

data_colors = pandas.DataFrame(data_dict)
data_colors.to_csv("New_Squirrel_Color_Data.csv")