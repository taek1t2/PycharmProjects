# # len(12345) #len doesn't like to read integers
#
# int("1234")
#
# print(int("1234") + int("1234"))
#
# int()
# float()
# str()
# bool()

name = input("Enter the name")
length_of_name = len(name)

print(type("Number of letters in your name: "))
print(type(length_of_name))

print("Number of letters in your name: " + str(length_of_name))