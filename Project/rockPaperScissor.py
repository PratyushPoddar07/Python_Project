
import random

while True:
    print("Enter your choice: \n 1 -> Rock \n 2 -> Paper \n 3 -> Scissors\n")

    user = int(input("Enter your choice: "))


    while user > 3 or user < 1:
        print("Enter a valid input")
        user = int(input("Enter your choice: "))  

    
    if user == 1:
        choice = 'Rock'
    elif user == 2:
        choice = 'Paper'
    else:
        choice = 'Scissors'

    # Computer's choice
    computer = random.randint(1, 3)
    if computer == 1:
        comp_choice = 'Rock'
    elif computer == 2:
        comp_choice = 'Paper'
    else:
        comp_choice = 'Scissors'

    print(f"User choice -> {choice} 'vs' Computer choice -> {comp_choice}")

    # Determine the winner
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 'Rock' and comp_choice == 'Scissors') or \
         (choice == 'Paper' and comp_choice == 'Rock') or \
         (choice == 'Scissors' and comp_choice == 'Paper'):
        result = 'User'
    else:
        result = 'Computer'

    # Print result
    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif result == 'User':
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

    # Ask if the user wants to play again
    print("Do you want to play again? (Y/N) ")
    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for playing!")
