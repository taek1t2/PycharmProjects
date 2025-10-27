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

beverage_options = input("What would you like? [Espresso / Latte / Cappuccino]: ")
def format_data(resources):
    resource_one = resources["water"]
    resource_two = resources["milk"]
    resource_three = resources["coffee beans"]
    if beverage_options == "report":
        print(f"Water: {resource_one}ml \nMilk: {resource_two}ml \nCoffee Beans:{resource_three}g")

format_data(resources)

turn_coffee_off = input("Done ordering? Type ['off']: \n").lower()

