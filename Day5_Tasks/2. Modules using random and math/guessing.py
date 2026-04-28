"""Create a Number Guessing Game where: 
● The program generates a random number between 1 and 50 using random. 
● The user has 5 attempts to guess the number."""

import random
import math
num = random.randrange(1, 50)

attempts = 5

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 50")
print("You have 5 attempts.\n")

for i in range(attempts):
    guess = int(input("Enter your guess: "))
    
    if guess == num:
        print("Congratulations! You guessed the number correctly!")
        break
    elif guess < num:
        print("Too low!")
    else:
        print("Too high!")
    
    print("Attempts left:", attempts - i - 1)

else:
    print("\n Sorry! You've used all attempts.")
    print("The correct number was:", num)

absolute_difference = math.fabs(num - guess)
print("So the guess is from the correct number is:",absolute_difference)
