# https://www.codewars.com/kata/58712dfa5c538b6fc7000569/train/python:

def count_red_beads(n):
    if n < 2:
        return 0
    return (n - 1) * 2

# https://www.codewars.com/kata/59a96d71dbe3b06c0200009c/train/python:

def generate_shape(n):
    return '\n'.join('+' * n for _ in range(n))


# https://www.codewars.com/kata/57ed30dde7728215300005fa/train/python:

def bumps(road):
    if road.count('n') <= 15:
        return "Woohoo!"
    else:
        return "Car Dead"


# https://www.codewars.com/kata/5a4138acf28b82aa43000117/train/python:

def adjacent_element_product(array):
    max_product = array[0] * array[1]  
    for i in range(1, len(array) - 1):
        product = array[i] * array[i + 1]
        if product > max_product:
            max_product = product
    return max_product

# https://www.codewars.com/kata/55b051fac50a3292a9000025/train/python:

def filter_string(st):
    return int(''.join([char for char in st if char.isdigit()]))
