print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")


bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You did not fill in the inputs.")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")


# # If/elif/else small pizza / my old code
# if size == small_bill:
#     print(f"Your final bill is: ${small_bill}")
# elif pepperoni == "Y":
#     add_pepperoni = 3
#     small_bill += add_pepperoni
#     print(f"Your final bill is: ${small_bill}")
# elif extra_cheese == "Y":
#     add_more_cheese = 1
#     small_bill += add_more_cheese
#     print(f"Your final bill is: ${small_bill}")
#
# # If/elif/else medium pizza
# if size == medium_bill:
#     print(f"Your final bill is: ${medium_bill}")
# elif pepperoni == "Y":
#     add_pepperoni = 3
#     medium_bill += add_pepperoni
#     print(f"Your final bill is: ${medium_bill}")
# elif extra_cheese == "Y":
#     add_more_cheese = 1
#     medium_bill += add_more_cheese
#     print(f"Your final bill is: ${medium_bill}")
#
# # If/elif/else large pizza
# if size == large_bill:
#     print(f"Your final bill is: ${large_bill}")
# elif pepperoni == "Y":
#     add_pepperoni = 3
#     large_bill += add_pepperoni
#     print(f"Your final bill is: ${large_bill}")
# elif extra_cheese == "Y":
#     add_more_cheese = 1
#     large_bill += add_more_cheese
#     print(f"Your final bill is: ${large_bill}")
