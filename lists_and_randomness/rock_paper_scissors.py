import random

print("Welcome to Rock Paper Scissors!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

choices = [rock, paper, scissors]
names = ["rock", "paper", "scissors"]

user_choice = input("What do you choose? Type 'Rock', 'Paper' or 'Scissors'.\n").lower()

if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
    print("You can only choose from the given options!")
else:
    machine_choice = random.choice(names)
    user_index = names.index(user_choice)
    machine_index = names.index(machine_choice)

    print("You chose:")
    print(choices[user_index])
    print("\n")
    print("Machine chose:")
    print(choices[machine_index])

    if user_index == machine_index:
        print("It's a tie!")
    elif (user_index - machine_index) % 3 == 1:
        print("✨ You Win! ✨")
    else:
        print("💥 You Lose! 💥")