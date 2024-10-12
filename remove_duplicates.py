# Bismillah
"""
Created on Sat Oct 12 21:41:23 2024

@author: Faxriddin
"""
from random import randint

def givingLists():
    numbers = []
    for i in range(20):
        numbers.append(randint(0, 10))
    return numbers

def removeDuplicates(myList):
    resultsList = set(myList).intersection(set(myList))
    return resultsList

# numbers = []
# for i in range(20):
#     numbers.append(randint(0, 10))
print(givingLists())
print(removeDuplicates(givingLists()))
