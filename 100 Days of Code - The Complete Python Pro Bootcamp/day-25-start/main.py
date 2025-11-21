# with open("weather_data.csv") as weather_deets:
#     for each_day in weather_deets:
#         weekly_weather = weather_deets.readlines()
#         print(weekly_weather)

import csv

with open("weather_data.csv", "r", newline='') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)





