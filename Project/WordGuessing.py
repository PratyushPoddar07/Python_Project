import random

name =input("What is your name? ")
print("Good Luck! ",name)
words =['rainbow','computer','science','player','math','jocker','water','board','guess','machine','ai']

words = random.choice(words)
guesses =''
turn =10

while turn >0:
    failed =0

    for char in words:
        if char in guesses:
            print(char,end=" ")

        else:
            print("_")
            failed += 1
    
    if failed == 0:
        print("You win ")
        print(f"The word is:  {words}")
        break

    print()
    guess = input("guess a character: ")

    guesses += guess

    if guess not in words:
        turn -= 1
        print("Wrong ")
        print(f"You have {turn} more guess")
        
        if turn == 0:
            print("You Loose")