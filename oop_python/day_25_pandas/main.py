# import csv
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temp = row[1]
#         if temp != "temp":
#             temperatures.append(int(temp))
#     print(temperatures)

###########################################################
# import csv
# import pandas
#
# data = pandas.read_csv("./weather_data.csv")
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
# avg = data["temp"].mean()
# max_value = data["temp"].max()
# max_temp = data[data.temp == data.temp.max()]
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# print(data)
# print(data_dict)
# print(temp_list)
# print(avg)
# print(max_temp)
# print(monday)
# print(monday_temp)

##############################################################
# import csv
# import pandas

# data_dict = {
#     "students": ["aman", "shreyansh", "ashish", "shivendra"],
#     "marks": [90, 72, 88, 79]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)

###############################################################
# import pandas
#
# data = pandas.read_csv("./squirrel_data.csv")
# no_of_gray = len(data[data["Primary Fur Color"] == "Gray"])
# no_of_black = len(data[data["Primary Fur Color"] == "Black"])
# no_of_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [no_of_gray, no_of_cinnamon, no_of_black]
# }
#
# count_data = pandas.DataFrame(data_dict)
# count_data.to_csv("./squirrel_count.csv")

#################################################
