# Randomisation - Mersenne twister
# random()

import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)
#
# random_float = random.uniform(1, 10)
# print(random_float)

flip_a_coin = random.randint(0, 1)
if flip_a_coin == 0:
    print("Heads")
else:
    print("Tails")
