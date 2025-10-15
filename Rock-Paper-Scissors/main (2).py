import random
print("Welcome to Rock Paper Scissors!")
print("Let's play best of 3 rounds!")

user_score = 0
computer_score = 0
round_number = 1

while round_number <= 3:
    print("\nRound", round_number)
    user_choice = input("Type Rock, Paper, Scissors:").lower()
    computer_choice =  random.choice(["rock", "paper", "scissors"])
    print("You chose:",user_choice)
    print("Computer chose:", computer_choice)
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You wins this round!")
            user_score = user_score + 1
        else:
            print("Computer wins this round!")
            computer_score = computer_score + 1
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win this round!")
            user_score = user_score + 1
        else:
            print("Computer wins this round!")
            computer_score = computer_score + 1
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win this round!")
            user_score = user_score + 1
        else:
            print("Computer wins this round!")
            computer_score = computer_score + 1
    
    else:
        print("invalid input.")
        continue
    print("Score: You =", user_score ,"Computer =", computer_score)
    
    if user_score == 2 or computer_score == 2:
        break
    round_number = round_number + 1
print("\nGame over!")
if user_score > computer_score:
    print("You won the game!")
elif computer_score > user_score:
    print("Computer won the game!")
else:
    print("It's a draw!")
        