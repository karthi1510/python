import random

print("welcome to rock paper scissors game!")
print("Type 'quit' to stop playing.\n")
user_score = 0
computer_score = 0

choices = ['rock' , 'paper' , 'scissors']
while True:
    user_choice = input("enter your chioce (rock, paper, scissors):").lower()
    if user_choice == 'quit':
        print("\n Thanks for playing!")
        print(f"Final score - you: {user_score} | computer:{computer_score}")
        break
    if user_choice not in choices:
        print("Invalid choice! please choose rock, paper, or scissors. \n")
        continue
    computer_choice = random.choice(choices)
    print(f"you chose: {user_choice}")
    print(f"computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("it's a tie!\n")
    elif (user_choice == 'rock' and computer_choice =='scissors') or \
    (user_choice == 'scissors' and computer_choice == 'paper') or \
    (user_choice == 'paper' and computer_choice =='rock'):
        print("You win this round!\n")
        user_score += 1
    else:
         print("computer wins this round!\n")
         computer_score += 1