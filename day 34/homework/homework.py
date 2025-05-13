# https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)


# https://www.codewars.com/kata/57e76bc428d6fbc2d500036d/train/python
def string_to_array(string):
    return string.split(" ")


# https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/python
def check(a, e):
    return e in a


# https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/python
def reverse_seq(n):
    return [i for i in range(n, 0, -1)]


# https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python
def count_by(x, n):
    return [x * i for i in range(1, n+1)]




def manual_min(numbers):
    if not numbers:
        raise ValueError("The list is empty")  
    
    min_value = numbers[0]  
    for num in numbers:
        if num < min_value:
            min_value = num  
    return min_value
numbers = [3, 1, 4, 1, 5, 9, -2]
print(manual_min(numbers)) 
print(manual_min([10, 20, 30]))  
print(manual_min([])) 




def manual_max(iterable):
    if not iterable:
        raise ValueError("The iterable cannot be empty")
    
    max_value = iterable[0]  
    for item in iterable:
        if item > max_value:  
            max_value = item
    return max_value
numbers = [3, 5, 7, 2, 8]
print(manual_max(numbers))