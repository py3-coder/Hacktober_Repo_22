import random

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

game_choice = [rock, paper, scissors]

user_choice = int(
    input(
        'what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'
    ))
print("You chose")
print(game_choice[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose")
print(game_choice[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You entered invalid no, You loose!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice == 2 and computer_choice == 0:
    print("You Loose!")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice > user_choice:
    print("You Loose!")
elif user_choice == computer_choice:
    print("It's Draw")

