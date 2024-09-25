# Bismillah
"""
Created on Wed Sep 25 22:05:03 2024

@author: Faxrddin
"""

text = 'Assalomu alaykum'
shift = 3

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    
    for char in message.lower():
        if char == ' ':
            encrypted_text += char 
        else:
            index = alphabet.find(char)
            # print(char)
            # new_index = (index + shift)%26 # if didn't write %26 there, the function will seek 27, 28 letter and will give IndexErorr
            new_index = (index + offset) % len(alphabet) # I did this to escape the counting mistakes
            # encrypted_text = alphabet[new_index]
            encrypted_text = encrypted_text + alphabet[new_index]   # In every cycle adding a letter to previous
        # print('char:', char, ' encrypted_text:', encrypted_text)
    
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

caesar(text, shift)
caesar(text, 9)
