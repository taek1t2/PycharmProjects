enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
def drink_potion():
    my_potions_stronger = 2
    print(my_potions_stronger)

drink_potion()
print(my_potions_stronger)

# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2

game()
print(player_health)
