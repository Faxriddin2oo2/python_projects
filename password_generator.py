# Bismillah
"""
Created on Sun Sep 29 17:24:22 2024

@author: Faxriddin
"""

# import secrets
# import string


# # Define the possible characters for the password
# letters = string.ascii_letters
# digits = string.digits
# symbols = string.punctuation

# # Combine all characters
# all_characters = letters + digits + symbols

# print(all_characters)
# print(secrets.choice(all_characters))

# import re
# import secrets
# import string


# def generate_password(length, nums, special_chars, uppercase, lowercase):
#     # Define the possible characters for the password
#     letters = string.ascii_letters
#     digits = string.digits
#     symbols = string.punctuation

#     # Combine all characters
#     all_characters = letters + digits + symbols

#     while True:
#         password = ''
#         # Generate password
#         for _ in range(length):
#             password += secrets.choice(all_characters)
        
#         constraints = [
#             (nums, r'\d'),
#             (lowercase, r'[a-z]'),
#             (uppercase, r'[A-Z]'),
#             (special_chars, r'\W')
#         ]        

#     return password
    
# # new_password = generate_password(8)
# # print(new_password)
# pattern = r'\W'
# quote = 'Not all those who wander are lost.'
# print(re.findall(pattern, quote))


# The final result
import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password
    
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)