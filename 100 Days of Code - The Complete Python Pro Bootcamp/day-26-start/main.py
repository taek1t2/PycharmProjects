
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