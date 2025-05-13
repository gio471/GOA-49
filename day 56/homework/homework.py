# https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/python:

def is_uppercase(inp):
    return inp == inp.upper()

# https://www.codewars.com/kata/56f69d9f9400f508fb000ba7/train/python:

def monkey_count(n):
    count = []
    i = 1
    while i <= n:
        count.append(i)
        i += 1
    return count

# https://www.codewars.com/kata/57a083a57cb1f31db7000028/train/python:

def powers_of_two(n):
    result = []
    i = 0
    while i <= n:
        result.append(2 ** i)
        i += 1
    return result

# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python:

def human_years_cat_years_dog_years(human_years):
    cat_years = 15  
    dog_years = 15  

    if human_years >= 2:
        cat_years += 9  
        dog_years += 9  

    if human_years > 2:
        cat_years += (human_years - 2) * 4  
        dog_years += (human_years - 2) * 5  

    return [human_years, cat_years, dog_years]

# https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/python:
def first_non_consecutive(arr):
    init = arr[0]
    for i in arr:
        if init != i:
            return i
        else:
            init += 1
    return None