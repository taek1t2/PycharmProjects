
from random import choice
from game_data import data

from art import logo, vs
print(logo)

def pick_a():
    compare_a = choice(data)
    return f"Compare A: {compare_a['name']}, {compare_a['description']}, {compare_a['country']}."
account_a = pick_a()
print(account_a)

print(vs)

def pick_b():
    compare_b = choice(data)
    return f"Against B: {compare_b['name']}, {compare_b['description']}, {compare_b['country']}."
account_b = pick_b()
print(account_b)

if account_a == account_b:
    account_b = choice(data)

pick_one = input("Who has more followers? Type 'a' or 'b': ").lower()
score = 0

def compare_counts(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    elif b_followers > a_followers:
        return user_guess == "b"
    else:
        return "Incorrect, please input either 'a' or 'b'."

a_followers_count = account_a[1]
b_followers_count = account_b[1]

is_correct = compare_counts(pick_one, a_followers_count, b_followers_count)

if is_correct:
    score +=1
    print(f"You're correct. Score: {score}")
else:
    print(f"Wrong, try again! Final Score: {score}")