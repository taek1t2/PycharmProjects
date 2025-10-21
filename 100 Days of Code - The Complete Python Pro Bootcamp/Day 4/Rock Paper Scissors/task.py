rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_art = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
import random

player_choice = player
print(f"You chose: {game_art[player_choice]}")

computer_choice = random.randint(0, 2)
print(f"Computer chose: {game_art[computer_choice]}")

if player_choice >= 3 or player_choice < 0:
    print("Error:Please list 0, 1, 2")
elif player_choice == computer_choice:
    print("It's a draw!")
elif player_choice == 0 and computer_choice == 2:
    print("You won!!!")
elif player_choice == 1 and computer_choice == 0:
    print("You won!!!")
elif player_choice == 2 and computer_choice == 1:
    print("You won!!!")
elif computer_choice == 0 and player_choice == 2:
    print("You lose!!!")
elif computer_choice == 1 and player_choice == 0:
    print("You lose!!!")
elif computer_choice == 2 and player_choice == 1:
    print("You lose!!!")



# Old code that I've approached
# if player1 == "0":
#     print(player_with_hands[0])
#     print(random.choice(computer_art))
# elif player1 == "1":
#     print(player_with_hands[1])
#     print(random.choice(computer_art))
# elif player1 == "2":
#     print(player_with_hands[2])
#     print(random.choice(computer_art))
# else:
#     print("Number error. Choose only 0, 1, 2")



