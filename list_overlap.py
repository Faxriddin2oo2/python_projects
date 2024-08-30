# Bismillah
"""
Created on Fri Aug 30 18:18:24 2024

@author: Faxriddin
"""


# write a program that returns a list that contains only the elements that are common between the lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# for number in a:
#     if number in b not in c:
#         c.append(number)
      
print(list(set(a).intersection(set(b))))