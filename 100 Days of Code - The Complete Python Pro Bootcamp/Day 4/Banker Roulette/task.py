friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

import random

print(random.choice(friends))

random_index = random.randint(0, 5)

print(friends[random_index])
