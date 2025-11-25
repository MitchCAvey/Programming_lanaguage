################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# # Local Scope - limited to the functions we define
# # See the example below

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
    
# drink_potion()
# # This will not work as this variable, as it's not define as
# # a Global Variable. 
# #print(postion_strength) 

# # Global Scope
# player_health = 10

# def drink_potion():
#     potion_strength = 2
#     print(player_health)
#     print(potion_strength)
    
# # Showing that Python doesn't have block scope
# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)

# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

# print(new_enemy)


# # How to use Global variables and modify their global value
# enemies = 1

# def increase_enemies():
#   global enemies
#   # is will only work if the you've called the global variable
#   # like above. E.g. using the 'global' keyword
#   enemies += 1  
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")    

# # Or you can simply return the variable like so
# enemies = 1

# def increase_enemies():  
#   print(f"enemies inside function: {enemies}")
#   return enemies + 1

# # We now call the increase_enemies function and save
# # this to the global variable, like so:
# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}") 


