# Faxriddin
"""
Created on Wed Sep 25 21:37:51 2024

@author: Faxriddin
"""

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# index=alphabet.find(text[0]) # When I give text[0] it returns '-1' because there is not 'H' but 'h' 
index =alphabet.find(text[0].lower()) # But when I write lower() function, if finds the right index
# print(index)
shifted = alphabet[index+shift]
# print(shifted)
for char in text:
    index = alphabet.find(char)
    # print(char)
    # print(index)
    # print(char, index)
    new_index = index + shift
    new_char = alphabet[new_index]
    print(new_char)