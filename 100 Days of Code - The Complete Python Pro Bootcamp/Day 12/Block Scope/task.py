game_level = 3
enemies = ['Skeleton', 'zombie', 'Alien']

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)