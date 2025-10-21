# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hey, {name}!")
    print(f"I'm from {location}")

greet_with("Tae", "South Korea")
greet_with("South Korea", "Tae") # It'll reverse

greet_with(name="Tae", location="South Korea") # Key Arguments
greet_with(location="South Korea", name= "Tae") # Positional Arguments

# def calculate_love_score(name, name2):
#     true_list = ["t", "r", "u", "e"]
#     love_list = ["l", "o", "v", "e"]
#
#     name = name.lower()
#     name2 = name2.lower()
#
#     first_digit = 0
#     second_digit = 0
#     for each_letter in true_list:
#         first_digit += name.count(each_letter)
#         first_digit += name2.count(each_letter)
#
#     for each_letter in love_list:
#         second_digit += name.count(each_letter)
#         second_digit += name2.count(each_letter)
#
#     love_score = int(str(first_digit) + str(second_digit))
#
#     print(f"Love score for {name} & {name2} is {love_score}")
#
# calculate_love_score("Kanye West", "Kim Kardashian")


