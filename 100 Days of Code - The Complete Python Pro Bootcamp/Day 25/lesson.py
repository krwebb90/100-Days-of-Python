# import csv
import pandas

# with open(r"/Users/webkerry/Documents/GitHub/100-Days-of-Python/100 Days of Code - The Complete Python Pro Bootcamp/Day 25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)


# with open(r"/Users/webkerry/Documents/GitHub/100-Days-of-Python/100 Days of Code - The Complete Python Pro Bootcamp/Day 25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pandas.read_csv("/Users/webkerry/Documents/GitHub/100-Days-of-Python/100 Days of Code - The Complete Python Pro Bootcamp/Day 25/weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# # pulling a column into a list of objects
# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data["temp"].mean())

# # print the row
# print(data[data.day == "Monday"])

# # print the row with the highest temp
# print(data[data.temp == data.temp.max()])

# # data = pandas.read_csv("/Users/webkerry/Documents/GitHub/100-Days-of-Python/100 Days of Code - The Complete Python Pro Bootcamp/Day 25/weather_data.csv")
# # print(data["temp"])


# # create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"]
#     , "scores": [76, 56, 65]
# }
# datatable = pandas.DataFrame(data_dict)
# print(datatable)

# # write to a new csv and put that file in the correct folder
# datatable.to_csv("/Users/webkerry/Documents/GitHub/100-Days-of-Python/100 Days of Code - The Complete Python Pro Bootcamp/Day 25/newdata.csv")



# squirrel data exercise

data = pandas.read_csv("/Users/webkerry/Documents/GitHub/100-Days-of-Python/100 Days of Code - The Complete Python Pro Bootcamp/Day 25/squirrel_count.csv")

# counting squirrels by color
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"]
    , "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)

df.to_csv("/Users/webkerry/Documents/GitHub/100-Days-of-Python/100 Days of Code - The Complete Python Pro Bootcamp/Day 25/squirrel_count_by_color.csv")