import random

user = int(input("Enter your range: "))
ranNum = random.randint(0,user)

chances =7
guessCount =0

for guessCount in range(0, chances):
    myguess = int(input("Please Enter your guess: "))

    if myguess == ranNum:
        print(f'The number is {ranNum}, and you guessed it right in {guessCount} attempt(s)! ')
        break
    elif myguess > ranNum:
        print("Your guess  is higher.")
    elif myguess < ranNum:
        print('Your guess is lower. ')
    
    if guessCount == chances:
        print(f'Oops,Sorry!  The number was {ranNum}. Better luck next time')