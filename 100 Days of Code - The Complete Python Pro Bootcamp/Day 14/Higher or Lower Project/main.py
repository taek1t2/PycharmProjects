
from random import choice
from game_data import data
from art import logo, vs


def pick_account():
    return choice(data)

account_a = pick_account()
account_b = pick_account()

if not account_a != account_b:
    account_b = choice(data)

def format_data(label, record):
    return f"{label}, {record['name']}, {record['description']} from {record['country']}"

def compare_counts(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    elif b_followers > a_followers:
        return user_guess == "b"
    else:
        return "Incorrect, please input either 'a' or 'b'."

print(logo)
continue_if_right = True
score = 0
account_a = choice(data)
while continue_if_right:

    account_b = choice(data)
    while account_a == account_b:
        account_b = choice(data)

    print(format_data("Compare A: ", account_a))
    print(vs)
    print(format_data("Against B: ", account_b))

    pick_one = input("Who has more followers? Type 'a' or 'b': ").lower()
    print("\n" * 30)

    a_followers_count = account_a['follower_count']
    b_followers_count = account_b['follower_count']

    is_correct = compare_counts(pick_one, a_followers_count, b_followers_count)

    if is_correct:
        score +=1
        print(f"You're correct. Score: {score}")
    else:
        print(f"Wrong, try again! Final Score: {score}")
        continue_if_right = False