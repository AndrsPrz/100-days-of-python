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
rps = [rock, paper, scissors]

try:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice >= 3 or user_choice < 0:
        print("You chose an invalid number, you lose!")
    else:
        print(rps[user_choice])

        computer_choice = random.randint(0,2)
        print(f"Computer chose: \n{rps[computer_choice]}")

        #Logic
        if user_choice == computer_choice:
            print("It's a draw")
        elif (user_choice == 0 and computer_choice == 2) or \
                (user_choice == 1 and computer_choice == 0) or \
                (user_choice == 2 and computer_choice == 1):
            print("You win!")
        else:
            print("You lose")

except ValueError:
    print("You typed an invalid character, you lose!")