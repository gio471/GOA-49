#https://www.codewars.com/kata/52ceafd1f235ce81aa00073a/train/python:

def plural(n):
    return n != 1


#https://www.codewars.com/kata/55a5bfaa756cfede78000026/train/python:

def problem(a):
    if isinstance(a, (int, float)):
        return a * 50 + 6
    else:
        return "Error"


#https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/python:

def multi_table(number):
    return '\n'.join([f"{i} * {number} = {i * number}" for i in range(1, 11)])


#https://www.codewars.com/kata/595970246c9b8fa0a8000086/train/python:

def capitalize_word(word: str) -> str:
    return word[0].upper() + word[1:]


#https://www.codewars.com/kata/56200d610758762fb0000002/train/python:

def add_five(num):
    total = num + 5
    return total
