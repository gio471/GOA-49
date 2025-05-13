# https://www.codewars.com/kata/56efc695740d30f963000557/train/python:

def to_alternating_case(string):
    return string.swapcase()

# https://www.codewars.com/kata/577bd026df78c19bca0002c0/train/python:

def correct(s):
    translation_table = str.maketrans("501", "SOI")
    return s.translate(translation_table)

# https://www.codewars.com/kata/56f6ad906b88de513f000d96/train/python:

def bonus_time(salary, bonus):
    if bonus:
        total_salary = salary * 10
    else:
        total_salary = salary
    
    return f"${total_salary}"

# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python:

def is_palindrome(s):
    s = s.lower()
    s = ''.join(e for e in s if e.isalnum())
    return s == s[::-1]

# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python:

def pig_it(text):
    words = text.split() 
    result = []
    
    for word in words:
        if word.isalpha():  
            result.append(word[1:] + word[0] + 'ay') 
        else:
            result.append(word)  
    
    return ' '.join(result)  

# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python:

def move_zeros(lst):
    non_zeros = [num for num in lst if num != 0]
    zeros = lst.count(0)
    return non_zeros + [0] * zeros