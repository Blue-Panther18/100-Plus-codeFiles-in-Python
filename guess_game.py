"""
This is a number guess game file.
It prompt a user to guess a randomly generated number between 1 to 10 (inclusive). 
The user only have 5 trials.
"""
import random

# Generate a random integer between 1-10.
num = random.randint(1, 10)
trail = 5

while(trail != 0):
    print(f"You have {trail} more trails\n")
    guess = int(input("Guess a number between 1-10: "))

    if(num == guess):
        print("Bravo!!! you've made the right guess.\n")
        break
    elif(num > guess):
        print("oops! your guess is smaller, try again.\n")
    else:
        print("oops! your guess is larger, try again.\n")
    trail -= 1

if(trail == 0):
    print("Game Over!!!")