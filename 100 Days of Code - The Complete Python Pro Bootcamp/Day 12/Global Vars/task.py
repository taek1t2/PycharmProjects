# Modifying Global Scope

enemies = "skeleton"


def increase_enemies():
    # global enemies
    enemies = "zombies"
    # enemies += "zombies"
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


