print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

the_route = input("Choose a direction: Left or Right")
choose_transportation = input("Choose which way you want to go: Swim or Wait?")
which_door = input("Which color door would you want to enter? Red, Blue or Yellow?")

#-----
# if the_route == "Left" or "left":
#     print(choose_transportation)
# elif the_route == "Right" or "right":
#     print("Fall into a hole. Game over.")
# else:
#     print(choose_transportation)
#-----

if the_route == "Left" or the_route == "left":
    if choose_transportation == "Swim" or "swim":
        print("Attacked by a sea monster. Game Over.")
    elif choose_transportation == "Wait" or "wait":
        if which_door == "Red":
            print("Burned by fire. Game Over.")
        elif which_door == "Blue":
            print("Eaten by beasts. Game Over.")
        elif which_door == "Yellow":
            print("You Win!!!")
        else:
            print("No door exists. Game Over")
elif the_route == "Right" or the_route == "right":
    print("Fall into a hole. Game Over.")
else:
    print("Must choose a path")





