# Bismillah
"""
Created on Tue Aug 27 17:57:13 2024

@author: Faxriddin
"""

# def odd_even():
#     ishora = True
#     while ishora:
#         number = int(input("Write down the number: "))
#         if number >= 0:    
#             if number%4 == 0:
#                 print("Given number is a multiple of 4")
#             elif number%2 == 0:
#                 print( "Given number is Even!")
#             else:
#                 print("Given number is Odd!")
#         else:
#             print("Please write the positive number! ")
#             continue
        
#         question = input("Do you want to continue? (Yes/No)")
        
#         if question == "No" or question == "no":
#             ishora = False

# print(odd_even())


def odd_even2():
    num = int(input("Print the first number: "))
    check = int(input("Print the number to divide first number: "))
    divide = num/check
    if divide%2 == 0:
        return "This divide is Even!"
    else:
        return "This divide is Odd!"
    
print(odd_even2())