import random

user_wins = 0
computer_wins = 0
options = ["Rock", "Paper", "Scissors"]


while True:
    user_input = input(" Type Rock , Paper or Scissors or press Q to quit ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    number_random = random.randint(0, 2)

# rock :0 paper : 1 Sissors 2
    computer_pick = options[number_random]

    print(f"computer picked {computer_pick } ")

    if user_input == "Rock" and computer_pick == "Scissors":

        print("you win ")

        user_wins += 1

    elif user_input == "Paper" and computer_pick == "Rock":
        print("you win ")
        user_wins += 1

    elif user_input == "Scissors" and computer_pick == "Paper":

        print("you win ")
        user_wins += 1

    else:
        print("you lost , try again please ")
        computer_wins += 1

    print(f"you won {user_wins} times.")
    print(f" the computer son {computer_wins} times .")

print("GoodBye")
