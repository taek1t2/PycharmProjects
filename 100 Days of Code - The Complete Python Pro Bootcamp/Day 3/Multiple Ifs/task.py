print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    want_photo = input("Do you want to have a photo taken? Type Y for Yes and N for No.")
    if want_photo == "Y" or "y":
        # Add $3 to their bill
        bill += 3

        print(f"Your final bill is ${bill}")
    # Still needs else in order for final bill to be totaled w/o photo

else:
    print("Sorry you have to grow taller before you can ride.")
