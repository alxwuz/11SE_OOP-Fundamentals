from game_objects import * # MUST have this in the program
import random # For random damage and health

# Create an instance of Player
player_list = [Player('Kelvin', 'Skeleton', 'Fisherman', 60, 35),
               Player('Lewis', 'Guofish', 'Zestyboi', 50, 50),
               Player('Shawn', 'Sheep', 'Cheater', 1, 1),
               Player('Nivel', 'Human', 'Theif', 3, 180)]

# TODO: Create an instance of Weapon with random damage between 12 and 15
weapon_list = [Weapon('Rod', 'Melee', random.randint(0, 15)),
               Weapon('Scales', 'Melee', random.randint(0, 0)),
               Weapon('Ram', 'Melee', random.randint(1, 144)),
               Weapon('Lockpick', 'Tool', random.randint(0, 0))]

# TODO: Create an instance of Enemy with random damage between 15 and 18, and random health between 80 and 140
enemy_shawn = Enemy('Shawn', 'Sheep', random.randint(15, 18), random.randint(80, 140))

# Print the player character details
print(f"Player Name: {player_list[0].name}")
print(f"Player Race: {player_list[0].race}")
print(f"Player Class: {player_list[0].cls}")
print(f"Player Attack: {player_list[0].atk}")
print(f"Player Health: {player_list[0].health}")

# TODO: Print the player weapon details
print(f"Weapon Name: {weapon_list[0].name}")
print(f"Weapon Name: {weapon_list[0].category}")
print(f"Weapon Name: {weapon_list[0].dmg}")

# TODO: Print the enemy character details
print(f"Enemy Name: {enemy_shawn.name}")
print(f"Enemy Name: {enemy_shawn.race}")
print(f"Enemy Name: {enemy_shawn.dmg}")
print(f"Enemy Name: {enemy_shawn.health}")

def selectplayer():
    selection = int(input('Choose a character 1-4: '))
    if selection == 1:
        current = player_list[0].name
        print(current)

    if selection == 2:
        current = player_list[1].name
        print(current)

    if selection == 3:
        current = player_list[2].name
        print(current)

    if selection == 4:
        current = player_list[3].name
        print(current)
selectplayer()

def selectweapon():
    selection = int(input('Choose a weapon 1-4: '))
    if selection == 1:
        current = weapon_list[0].name
        print(current)

    if selection == 2:
        current = weapon_list[1].name
        print(current)

    if selection == 3:
        current = weapon_list[2].name
        print(current)

    if selection == 4:
        current = weapon_list[3].name
        print(current)
selectweapon()

