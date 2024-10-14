# Bismillah
"""
Created on Wed Oct  9 22:11:41 2024

@author: Faxriddin
"""
# function view
def fibonacci(count):
    if count <= 0:
        return []
    if count == 1:
        return [0]
    if count == 2:
        return [0,1]
    
    fib_sequence = [0,1]
    for n in range(2, count):
        fib_sequence.append(fib_sequence[n-1]+fib_sequence[n-2])
        
    return fib_sequence

# print(fibonacci(4))


# class view
class Solution():
    def fibonacci(self, count):
        if count <= 0:
            return []
        if count == 1:
            return [0]
        if count == 2:
            return [0,1]
        
        fib_sequence = [0,1]
        for n in range(2, count):
            fib_sequence.append(fib_sequence[n-1]+fib_sequence[n-2])
            
        return fib_sequence
    
solution = Solution()
print(solution.fibonacci(5))