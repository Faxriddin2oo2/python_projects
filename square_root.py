# Bismillah
"""
Created on Sat Sep 28 21:00:19 2024

@author: Faxriddin
"""

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root

N = 16
square_root_bisection(N)





def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dash_line = ""
    answer_line = ""

    for problem in problems:
        parts = problem.split()

        if parts[1] not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not (parts[0].isdigit() and parts[2].isdigit()):
            return "Error: Numbers must only contain digits."

        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the width of the problem (largest number + operator + 2 spaces)
        width = max(len(parts[0]), len(parts[2])) + 2

        # Prepare each line of the arranged problems
        first_line += parts[0].rjust(width) + "    "
        second_line += parts[1] + parts[2].rjust(width - 1) + "    "
        dash_line += "-" * width + "    "

        if show_answers:
            if parts[1] == '+':
                answer = str(int(parts[0]) + int(parts[2]))
            else:
                answer = str(int(parts[0]) - int(parts[2]))
            answer_line += answer.rjust(width) + "    "

    # Remove the trailing spaces
    first_line = first_line.rstrip()
    second_line = second_line.rstrip()
    dash_line = dash_line.rstrip()
    answer_line = answer_line.rstrip()

    if show_answers:
        return first_line + "\n" + second_line + "\n" + dash_line + "\n" + answer_line
    else:
        return first_line + "\n" + second_line + "\n" + dash_line

# Example usage
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
