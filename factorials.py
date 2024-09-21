# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 18:29:19 2024

@author: asus
"""

def factorial():
    N = int(input("Qaysi sonni factorialini bilishni istaysiz?\n>>>"))
    i = 1
    factorial = 1
    while True:
        if i-1 != N:
            factorial = factorial*i
            i += 1            
        else:
            break
        
    return factorial




print(factorial())
