# Bismillah
"""
Created on Mon Oct  7 21:05:34 2024

@author: Faxriddin
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
commonsList = []
for x in a:
    if x in b:
        commonsList.append(x)

commonsList = set(commonsList)
print(commonsList)