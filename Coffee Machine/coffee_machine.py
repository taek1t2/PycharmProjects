MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee beans": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee beans": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee beans": 24,
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
        if ingredients[item] >= resources[item]:
            print(f"Sorry, there aren't enough {item}.")
            return False
    return True

def process_coins():
    """To insert coins and add the total after inserting"""
    print("Please insert coins.")
    total = float(input("Add Quarters: ")) * 0.25
    total += float(input("Add Dimes: ")) * 0.1
    total += float(input("Add Nickels: ")) * 0.05
    total += float(input("Add Pennies: ")) * 0.01
    return total


def check_transaction(received_money, drink_cost):
    """Return true when the payment is accepted, or False if money is insufficient."""
    if received_money >= drink_cost:
        change = round(received_money - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")

while True:
    beverage_options = input("What would you like? [Espresso / Latte / Cappuccino]: ")
    if beverage_options == "off":
        print("Order is finished, good-bye")
        break
    elif beverage_options == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee Bean: {resources["coffee beans"]}g")
        print(f"Profit: ${profit}")
    else:
        drink = MENU[beverage_options]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if check_transaction(payment, drink['cost']):
                make_coffee(beverage_options, drink["ingredients"])

