from art import logo
print(logo)
welcome = input("Hi! I'm a basic calculator. Click 'Enter' to continue")
print(welcome)

user_choose = input("Please select an operation: '+', '-', '*', '/'\n")

n1 = int(input("Input the first number: "))
n2 = int(input("Input the second number: "))

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

if user_choose in operations:
    chosen_function = operations[user_choose]
    answer = chosen_function(n1, n2)
    print(answer)

to_continue_more = True
while to_continue_more:
    continue_calculating = input("Do you want to perform another calculation? ('y'/'n') \n").lower()
    if continue_calculating == "y":
        n1 = answer
        user_choose = input("Please select an operation: '+', '-', '*', '/'\n")
        n2 = int(input("Input the second number: \n"))
        if user_choose in operations:
            chosen_function = operations[user_choose]
            answer = chosen_function(n1, n2)
            print(answer)
    else:
        to_continue_more = False
        print(f"This is your final answer: {answer}")

