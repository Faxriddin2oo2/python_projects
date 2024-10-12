# Bismillah
"""
Created on Sat Oct 12 21:55:13 2024

@author: Faxriddin
"""

def reverseWord(sentence):
    """ This function will return reversed verse of the sentence"""
    splitted = sentence.split()
    finalResult = ' '.join(splitted[::-1])
    return finalResult
    
sent = "This is the long sentence"
print(reverseWord(sent))