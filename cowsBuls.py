# Bismillah
"""
Created on Sun Oct 13 20:09:26 2024

@author: Faxriddin
"""
import random

class Solution(object):
    def __init__(self):
        # Generate a random 4-digit number as a string
        self.secret_number = str(random.randint(1000, 9999))
        self.guess_count = 0

    def get_cows_and_bulls(self, guess):
        cows, bulls = 0, 0
        for i in range(4):
            if guess[i] == self.secret_number[i]:
                cows += 1
            elif guess[i] in self.secret_number:
                bulls += 1
        return cows, bulls

    def play_game(self):
        print("Welcome to the Cows and Bulls game!")
        print("I have generated a 4-digit number. Try to guess it.")

        while True:
            guess = input("Enter your 4-digit guess: ")
            if len(guess) != 4 or not guess.isdigit():
                print("Please enter a valid 4-digit number.")
                continue

            self.guess_count += 1
            cows, bulls = self.get_cows_and_bulls(guess)

            if cows == 4:
                print(f"Congratulations! You guessed the correct number {self.secret_number} in {self.guess_count} guesses.")
                break
            else:
                print(f"{cows} cows, {bulls} bulls. Try again!")

# To play the game:
game = Solution()
game.play_game()
