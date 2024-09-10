# Bismillah
"""
Created on Tue Sep 10 21:00:29 2024

@author: Faxriddin
"""

# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
# then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)

import random as r

def guess_num():
    guesses=0
    print("Let's play a guessing game!")
    a = r.randint(0, 10)
    num = input("I thought the number from 1 to 9 can you guess")

    while True:
        guesses +=  1
        m = int(input("Guess the number \n>>>"))
        if m > a:
            print("Your number is bigger!")
            continue
        elif m<a:
            print("Your number is smaller!")
            continue
        else:
            print(f"Your guess is right!!!"
                  f"You found it in {guesses} attempts")
        
guess_num()
