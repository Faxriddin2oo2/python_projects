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
    
    for char in message.lower(): # Making any message into lower letters
        if char == ' ': # If char is empty then encrypted text also the same
            encrypted_text += char 
        else: 
            index = alphabet.find(char) # 'index' will search the location of index of every single letter of word in alphabet list
            # print(char)
            # new_index = (index + shift)%26 # if didn't write %26 there, the function will seek 27, 28 letter and will give IndexErorr
            
            # Below we can see how we add some number to the current number of index, then we took result of this and every letter before will change to another
            new_index = (index + offset) % len(alphabet) # I did this to escape the counting mistakes
            # encrypted_text = alphabet[new_index]
            encrypted_text = encrypted_text + alphabet[new_index]   # In every cycle adding a letter to previous
        # print('char:', char, ' encrypted_text:', encrypted_text)
    
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

# caesar(text, shift)
# caesar(text, 9)



import string

letters = string.ascii_lowercase
text = 'Hello world'
shift = 4


def ceasar_cipher(text, offset):
    encrypted_text = ''
    for char in text:
        if char == ' ':
            encrypted_text += char
        else:
            index = letters.find(char)
            new_index = (index+offset)%len(letters)
            encrypted_text += letters[new_index]
        
    print('Input: ', text)
    print('Output: ', encrypted_text)


ceasar_cipher(text, shift)
ceasar_cipher('bir bir', 3)
    


































