# Bismillah
"""
Created on Fri Aug 30 22:27:20 2024

@author: Faxriddin
"""



# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)
word = input("Give the word and I'll check this word palindrome or not: ").lower()
print("This string is palindrome") if word[0:] == word[-1::-1] else print("This string is not palindrome")