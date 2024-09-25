# Bismillah
"""
Created on Wed Sep 25 22:05:03 2024

@author: Faxrddin
"""

text = 'Assalomu alaykum'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

for char in text.lower():
    if char == ' ':
        encrypted_text += char 
    else:
        index = alphabet.find(char)
        # print(char)
        new_index = (index + shift)%26
        # encrypted_text = alphabet[new_index]
        encrypted_text = encrypted_text + alphabet[new_index]   # In every cycle adding a letter to previous
    print('char:', char, ' encrypted_text:', encrypted_text)