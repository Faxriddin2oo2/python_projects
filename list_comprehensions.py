# Bismillah
"""
Created on Sun Sep  8 22:34:50 2024

@author: Faxriddin
"""
# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(list(num for num in a if num%2==0))