enemies = 1


# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outsidetask.py function: {enemies}")

# Local Scope
# def drink_potions():ß
#     potion_strength = 2
#     print(f"Potion strength  inside function: {potion_strength}")
#
# drink_potions()
# print(potion_strength)

#Global Scope
# player_heath = 10
#
# def game():
#     def drink_potions():
#         potion_strength = 2
#         print(player_heath)
#     drink_potions()
#
# game()
# print(player_heath)

# L — Local     → inside the current function
# E — Enclosing  → any outer (but not global) function
# G — Global     → module-level (the .py file itself)
# B — Built-in   → Python's own names: print, len, range…

enemies = 1              # ← G (global)

def game():
    def drink_potions():
        potion_strength = 2  # ← L (local to drink_potions)
        print(enemies)       # L? no → E? no → G? yes ✓
    drink_potions()

game()
print(enemies)           # still 1 — global was never touched