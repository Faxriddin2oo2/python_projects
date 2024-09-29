# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:24:22 2024

@author: asus
"""

import secrets
import string


# Define the possible characters for the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols
print(all_characters)
print(secrets.choice(all_characters))