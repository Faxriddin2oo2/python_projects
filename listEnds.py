# Bismillah
"""
Created on Wed Oct  9 22:00:03 2024

@author: Faxriddin
"""

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.

import random

def listEnds(arr):
    new_list = []
    new_list.append(arr[0])
    new_list.append(arr[-1])
    return new_list

array = [5, 10, 15, 20, 25]
list_numbers = list(random.sample(range(30), random.randint(2, 10)))
print(listEnds(list_numbers))