# 1) https://www.codewars.com/kata/56b7f2f3f18876033f000307/train/python:

def in_asc_order(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


# 2) https://www.codewars.com/kata/5663f5305102699bad000056/train/python:

def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1

    len_a1_min = min(len(x) for x in a1)
    len_a1_max = max(len(x) for x in a1)
    len_a2_min = min(len(x) for x in a2)
    len_a2_max = max(len(x) for x in a2)
    

    return max(abs(len_a1_max - len_a2_min), abs(len_a1_min - len_a2_max))


# 3) https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/train/python:

def flatten_and_sort(array):

    return sorted([item for sublist in array for item in sublist])

# 4) https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/python:

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 5) https://www.codewars.com/kata/5300901726d12b80e8000498/train/python:

def fizzbuzz(n):
    result = []
    
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    
    return result

# 6) https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/train/python:

def row_weights(array):
    team_1_weight = sum(array[i] for i in range(0, len(array), 2))  
    team_2_weight = sum(array[i] for i in range(1, len(array), 2))  
    return (team_1_weight, team_2_weight)

# 7) https://www.codewars.com/kata/535474308bb336c9980006f2/train/python:

def greet(name):
    return "Hello " + name.capitalize() + "!"


# 8) https://www.codewars.com/kata/580a4734d6df748060000045/train/python:

def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return "yes, ascending"
    elif arr == sorted(arr, reverse=True):
        return "yes, descending"
    else:
        return "no"


# 9) https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/python:

def remove_duplicate_words(s):
    words = s.split()  
    seen = set()  
    result = []  

    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)

    return ' '.join(result)  