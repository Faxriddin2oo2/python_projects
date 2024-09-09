# Bismillah
"""
Created on Mon Sep  9 20:56:44 2024

@author: Faxriddin
"""
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
# print out a message of congratulations to the winner, and ask if the players want to start a new game)
print("Let's playing  Scissors, Paper, Rock ")
"paper"<"rock"
"rock"<"scissors"
"scissors"<"paper"
while True:
    a=input("Player a, please choose(Scissors, Paper, Rock)").lower()
    b=input("Player a, please choose(Scissors, Paper, Rock)").lower()
    if a=="paper" and b=="rock":
        print("Player a won")
    elif a=="rock" and b=="scissors":
        print("Player a won")
    elif a=="scissors" and b=="paper":
        print("Player a won")
    elif b=="paper" and a=="rock":
        print("Player b won")
    elif b=="rock" and a=="scissors":
        print("Player b won")
    elif b=="scissors" and a=="paper":
        print("Player b won")
    elif a==b:
        print("Draw!")
    else:
        print("Please give the right options!")
        
    question=input("Would you like to continue(yes/no): ")
    if question == "yes":
        continue
    else:
        break
    
print("This is end of the game!")