#file not found
# with open("a_file.txt") as file:
#     file.read()

#KeyError
# a_dict = {"key": "value"}
# value = a_dict["non_existent_key"]

#IndexError
# fruit_list = ["apple", "banana", "orange"]
# fruit = fruit_list[4]

#TypeError
# text = "abc"
# print(text + 5)

try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error:
    print(f"That {error} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File is closed.")

raise KeyError
