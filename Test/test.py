import random

number = random.randint(1,9)
correct = False

while correct == False:
    guess = int(input("Guess a number from 1-9\n"))
    if guess == number:
        print("You guessed correct")
        correct = True
    else:
        print("Wrong, guess again.")
