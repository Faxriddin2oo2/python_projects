#Bismillah
"""
Created on Mon Oct  7 21:18:57 2024

@author: Faxriddin
"""

def checkPrimality():
    print("You should give number, then I guess it prime or not!")
    question = int(input("Give me a number:"))
    x = list(range(2, question))
    for num in x:
        divisors = [i for i in x if question%i==0]
        if question%num == 0:
            # divisors.append(num)
            return f"This number isn't prime, so it have this divisors: {divisors}"
        return 'This number is prime'
    
print(checkPrimality())