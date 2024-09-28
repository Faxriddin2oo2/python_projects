# Bismillah
"""
Created on Sat Sep 28 20:58:28 2024

@author: Faxriddin
"""

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = ""
    second_line = ""
    dash_line = ''
    answer_line = ''
    
    for problem in problems:
        parts = problem.split() # Split to three elements each element of main list
        # print(parts)
        
        if parts[1] not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        
        if not (parts[0].isdigit() and parts[2].isdigit()):
            return "Error: Numbers must only contain digits."
        if len(parts[0])>4 or len(parts[2])>4:
            return "Error: Numbers cannot be more than four digits."
        
        width = max(len(parts[0]), len(parts[2])) + 2
        
        first_line += parts[0].rjust(width) + "    "
        second_line += parts[1] + parts[2].rjust(width-1) + "    "
        dash_line += "-"*width + "    "
        
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
        
        
    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}' )