# Bismillah
"""
Created on Wed Aug 28 17:20:50 2024

@author: Faxriddin
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b=[]

# for number in a:
#     if number < 5:
#         b.append(number)
        
# print(b)
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python
# print([num for num in a if num<5])


# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by 
# the user.
number = int(input("Give a number: "))
print([num for num in a if num<number])


