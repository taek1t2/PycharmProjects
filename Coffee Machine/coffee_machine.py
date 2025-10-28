MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee beans": 100,
}

profit = 0

def is_resources_sufficient(ingredients):
    """Returns True if order can made, false if ingredients are insufficient"""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there aren't enough {item}.")
            return False
        return True

def process_coins():
    """To insert coins and add the total after inserting"""
    print("Please insert coins.")
    total = float(input("Quarters: ")) * 0.25
    total += float(input("Dimes: ")) * 0.1
    total += float(input("Nickels: ")) * 0.05
    total += float(input("Pennies: ")) * 0.01

process_coins()

while True:
    beverage_options = input("What would you like? [Espresso / Latte / Cappuccino]: ")
    if beverage_options == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee Bean: {resources["coffee beans"]}g")
        print(f"Water: ${profit}")
    elif beverage_options == "off":
        print("Order is finished, good-bye")
    break
