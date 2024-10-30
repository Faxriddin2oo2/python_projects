# Bismillah
"""
Created on Wed Oct 30 19:04:02 2024

@author: Faxriddin
"""

def isLeapYear():
    year = int(input("Give me a year: "))
    if year%100 == 0:
        if year%400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is a normal year")
    elif year%4 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is a normal year")

isLeapYear()