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

machine_choice = random.choice(['rock', 'paper', 'scissors'])

user_choice = input("What do you choose? Type 'Rock', 'Paper' or 'Scissors'.\n").lower()

if user_choice == machine_choice:
    play_again = input("It's a tie! Play again? Type 'Y' for Yes or 'N' for No.\n")
    if play_again == 'Y':
        user_choice = input("What do you choose? Type 'Rock', 'Paper' or 'Scissors'.\n").lower()
        machine_choice = random.choice(['rock', 'paper', 'scissors'])
        if user_choice == "rock" and machine_choice == "paper":
            print(rock,"\n")
            print(f"machine chose {paper}")
            print("💥 You Lose! 💥")
        elif user_choice == "rock" and machine_choice == "scissors":
            print(rock,"\n")
            print(f"machine chose {scissors}")
            print("✨ You Win! ✨")
        elif user_choice == "paper" and machine_choice == "rock":
            print(paper,"\n")
            print(f"machine chose {rock}")
            print("✨ You Win! ✨")
        elif user_choice == "paper" and machine_choice == "scissors":
            print(paper,"\n")
            print(f"machine chose {scissors}")
            print("💥 You Lose! 💥")
        elif user_choice == "scissors" and machine_choice == "rock":
            print(scissors,"\n")
            print(f"machine chose {rock}")
            print("💥 You Lose! 💥")
        elif user_choice == "scissors" and machine_choice == "paper":
            print(scissors,"\n")
            print(f"machine chose {paper}")
            print("✨ You Win! ✨")
    else:
        print("Goodbye!")
elif user_choice == "rock" and machine_choice == "paper":
    print(rock,"\n")
    print(f"machine chose {paper}")
    print("💥 You Lose! 💥")
elif user_choice == "rock" and machine_choice == "scissors":
    print(rock,"\n")
    print(f"machine chose {scissors}")
    print("✨ You Win! ✨")
elif user_choice == "paper" and machine_choice == "rock":
    print(paper,"\n")
    print(f"machine chose {rock}")
    print("✨ You Win! ✨")
elif user_choice == "paper" and machine_choice == "scissors":
    print(paper,"\n")
    print(f"machine chose {scissors}")
    print("💥 You Lose! 💥")
elif user_choice == "scissors" and machine_choice == "rock":
    print(scissors,"\n")
    print(f"machine chose {rock}")
    print("💥 You Lose! 💥")
elif user_choice == "scissors" and machine_choice == "paper":
    print(scissors,"\n")
    print(f"machine chose {paper}")
    print("✨ You Win! ✨")
