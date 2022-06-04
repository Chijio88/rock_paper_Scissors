import random


rock = 'R'
Scissors = 'S'
Paper = 'P'
Allowed = set("RPS! .")

while True:
    userAction = input("Enter a choice (R, P, S): ")
    possibleActions = ["R", "P", "S"]
    computer_action = random.choice(possibleActions)
    print(f"\nPlayer: {userAction}, computer: {computer_action}.\n")

    if userAction == computer_action:
        print(f"Both players selected {userAction}. It's a tie!")
    elif userAction == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif userAction == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif userAction == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
            
    if userAction and Allowed.issuperset(userAction):
        break
    print("Invalid Input from Player!. Try again..")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
    