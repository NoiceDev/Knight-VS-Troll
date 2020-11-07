#  _  __     _      _   _    __   _____   _____        _ _  1.0
# | |/ /_ _ (_)__ _| |_| |_  \ \ / / __| |_   _| _ ___| | |
# | ' <| ' \| / _` | ' \  _|  \ V /\__ \   | || '_/ _ \ | |
# |_|\_\_||_|_\__, |_||_\__|   \_/ |___/   |_||_| \___/_|_|
#             |___/

# A fun project for school. You can use the code or whatever.

#  _    _ _                 _
# | |  (_) |__ _ _ __ _ _ _(_)___ ___
# | |__| | '_ \ '_/ _` | '_| / -_|_-<
# |____|_|_.__/_| \__,_|_| |_\___/__/

# Importing some libraries that are needed for the project to function.

# Importing libraries.
import random
import time
import sys

# __   __        _      _    _          __       _    _    _
# \ \ / /_ _ _ _(_)__ _| |__| |___ ___ / _|___  | |  (_)__| |_ ___
#  \ V / _` | '_| / _` | '_ \ / -_|_-< > _|_ _| | |__| (_-<  _(_-<
#   \_/\__,_|_| |_\__,_|_.__/_\___/__/ \_____|  |____|_/__/\__/__/

# Variablers and lists that I need for the project to work.

# Lists that are used in functions.
knightHits = ["[The knight slashed at the troll.]", "[The knight kicked the troll.]", "[The knight took off his armour and unleashed his 4 inches, hitting the troll.]"]
knightHeals = ["[The knight heals.]", "[The knight drinks a mini.]"]
trollHits = ["[The troll bit the knight.]"]
trollHeals = ["[The troll drank some blood.]"]

# Variables.
knightHealth = 1
trollHealth = 1

#  ___             _   _
# | __|  _ _ _  __| |_(_)___ _ _  ___
# | _| || | ' \/ _|  _| / _ \ ' \(_-<
# |_| \_,_|_||_\__|\__|_\___/_||_/__/

# Functions n stuff.

def displayHP():
    print("[Player Health:", str(knightHealth) + "]")
    print("[Troll Health:", str(trollHealth) + "]")

#   ___                
#  / __|__ _ _ __  ___ 
# | (_ / _` | '  \/ -_)
#  \___\__,_|_|_|_\___|

# The game itself.

print("""
  _  __     _      _   _    __   _____   _____        _ _  1.0
 | |/ /_ _ (_)__ _| |_| |_  \ \ / / __| |_   _| _ ___| | |
 | ' <| ' \| / _` | ' \  _|  \ V /\__ \   | || '_/ _ \ | |
 |_|\_\_||_|_\__, |_||_\__|   \_/ |___/   |_||_| \___/_|_|
             |___/
""")

while True:

    # Health variables that reset at the start of every game.
    knightHealth = random.randint(10, 25)
    trollHealth = random.randint(10, 25)

    print("[Fight ⚔]")
    print("[The fight begins...]")
    displayHP()
    input()

    # Chooses randomly from the actions.
    while True:

        # Picks action.
        action = random.randint(1, 25)
        if action == 1 or action == 2 or action == 3 or action == 4 or action == 5 or action == 6 or action == 7 or action == 8 or action == 9 or action == 10:  # Knight hits enemy.

            damage = random.randint(1, 2)

            trollHealth = trollHealth - damage
            print(random.choice(knightHits))


            displayHP()
        elif action == 11 or action == 12 or action == 13 or action == 14 or action == 15 or action == 16 or action == 17 or action == 18 or action == 19 or action == 20:  # Troll hits player.
            damage = random.randint(1, 2)
            knightHealth = knightHealth - damage
            print(random.choice(trollHits))
            displayHP()
        elif action == 21 or action == 22:  # Knight heals.
            heal = random.randint(1, 5)

            knightHealth = knightHealth + heal
            print(random.choice(knightHeals))

            displayHP()

        elif action == 23 or action == 24:  # Troll heals.

            heal = random.randint(1, 5)

            trollHealth = trollHealth + heal
            print(random.choice(trollHeals))

            displayHP()
        else:
            print("[Nothing happened...]")

        # Waits for player to press enter to continue.
        input()

        if knightHealth < 1:
            knightDeaths = ["[The knight fell, he ded.]"]
            print("[The knight died.]")
            input()
            break

        elif trollHealth < 1:
            trollDeaths = ["[The troll bled to death.]"]
            print(random.choice(trollDeaths))
            input()
            break
