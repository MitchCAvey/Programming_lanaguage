
import csv
import pandas
import random

WORK_FILE_DIRECTORY = "./Python/PythonBootCampt/Day25"
HOME_FILE_DIRECTORY = "./PersonalSource/Python/PythonBootCampt/Day25"

# with open(".\Python\PythonBootCampt\Day25\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# temperatures = []
# with open(".\Python\PythonBootCampt\Day25\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#             # print(row)
#     print(temperatures)


# data = pandas.read_csv(f"{FILE_DIRECTORY}/weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()

# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# average_temp = sum(temp_list) / len(temp_list)

# print(average_temp)

# print(data["temp"].mean())

# print(data["temp"].max())


# Get data in Columns
# print(data["condition"])

# print(data.condition)

# Get data in Rows
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# # print(data)

data = pandas.read_csv(f"{WORK_FILE_DIRECTORY}/SquirrelCensusData.csv")
graySquirrels = len(data[data["Primary Fur Color"] == "Gray"])
redSquirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
blackSquirrels = len(data[data["Primary Fur Color"] == "Black"])
print(graySquirrels)
print(redSquirrels)
print(blackSquirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [graySquirrels, redSquirrels, blackSquirrels]
}

# print(data_dict)

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv(f"{WORK_FILE_DIRECTORY}/squirrel_count.csv")




