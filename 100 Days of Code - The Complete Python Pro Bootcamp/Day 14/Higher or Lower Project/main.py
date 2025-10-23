
from random import choice
from game_data import data

from art import logo, vs
print(logo)

def pick_a():
    compare_a = choice(data)
    return f"Compare A: {compare_a['name']}, {compare_a['description']}, {compare_a['country']}."
option_a = pick_a()
print(option_a)

print(vs)

def pick_b():
    compare_b = choice(data)
    return f"Against Compare B: {compare_b['name']}, {compare_b['description']}, {compare_b['country']}."
option_b = pick_b()
print(option_b)

pick_one = str(input("Who has more followers? Type 'A' or 'B': ")).lower()