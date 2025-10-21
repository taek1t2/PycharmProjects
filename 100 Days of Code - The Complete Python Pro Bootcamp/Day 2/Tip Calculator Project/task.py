print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# Revised Code - Since it was only showing one decimal, the correction is...
tip_from_percentage = tip / 100
bill_with_tip = bill * (1 + tip_from_percentage)
total = bill_with_tip / people
final_amount = round(total, 2)

print(f"$ {final_amount:.2f}") # Needed a 2nd opinion from chatty and according to AI...
# #round() will always return as a float even with one decimal. Will not show 0 in 2nd decimal.

#instructor's input
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
#
# print(f"${final_amount}") #still shows as one decimal if the bill is a total of no decimal e.g 150


# Original Code:
# tip_from_percentage = tip / 100
# add_with_one = 1 + tip_from_percentage
# total = (bill * tip_from_percentage) / people
# final_amount = round(total, 2)
#
# print("$" + str(final_amount))
