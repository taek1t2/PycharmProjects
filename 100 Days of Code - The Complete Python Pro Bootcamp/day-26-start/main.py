
#List Comprehension [new_item for item in list]
#python sequence - range, tuple, list, strings

numbers = [1, 2, 3]
new_list = [n * 2 for n in numbers]
print(new_list)


my_name = "Taeyeon Kim"
each_alpha = [letter for letter in my_name]
print(each_alpha)

list_in_range = range(1, 5)
new_range_list = [num * 2 for num in list_in_range]
print(new_range_list)

#or

new_list_num = [new_num * 2 for new_num in range(1, 8)]
print(new_list_num)

names = ["Ann", "Nara", "Beth", "Diana", "Hyesook", "Taeyeon"]
shorter_name = [name for name in names if len(name) < 5]
print(shorter_name)

all_caps_name = [name.upper() for name in names if len(name) > 4]
print(all_caps_name)

#dictionary comprehension: variable = {new_key:new_value for (new_key, new_value) in dict.items()}
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_as_items = sentence.split()

result = {word:len(word) for word in word_as_items}
print(result)

#panda columns, rows and charts for loops
import pandas
student_dict = {}
students_data_frame = pandas.DataFrame(student_dict)
for (index, row) in students_data_frame.iterrows():
    print(index)