# Guessing Game
import random
m=int(input("Enter the maximum limit of the guessing game: "))
Val = random.randint(1, m)
guess= int(input("Guess the random integer: "))
while guess!=Val:
    if guess>Val:
        print("high")
        guess= int(input("Guess the random integer: "))
    else:
        print("low")
        guess= int(input("Guess the random integer: "))
if guess==Val:
    print("Correct!")
