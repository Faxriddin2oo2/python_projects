# Bismillah
"""
Created on Thu Aug 29 17:38:23 2024

@author: Faxriddin
"""

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
#  For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

number = int(input("Give the number: "))
x = list(range(2,number))

print(f"Divisors for the {number} are:")
print([i for i in x if number%i==0])