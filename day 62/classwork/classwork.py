# https://www.codewars.com/kata/5ad0d8356165e63c140014d4/train/python:

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0

# https://www.codewars.com/kata/5ae62fcf252e66d44d00008e/train/python:

def expression_matter(a, b, c):
    expressions = [
        a + b + c,
        a * b * c,
        a + (b * c),
        (a + b) * c,
        a * (b + c),
        (a * b) + c
    ]
    return max(expressions)


# https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python:

def sum_str(a, b):
    a = int(a) if a else 0
    b = int(b) if b else 0
    return str(a + b)

# https://www.codewars.com/kata/57f24e6a18e9fad8eb000296/train/python:

def how_much_i_love_you(nb_petals):
    phrases = [
        "I love you", 
        "a little", 
        "a lot", 
        "passionately", 
        "madly", 
        "not at all"
    ]
    return phrases[(nb_petals - 1) % 6]


# https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b/train/python:

def reverse_list(l):
    return l[::-1]


# https://www.codewars.com/kata/58cb43f4256836ed95000f97/train/python:
def find_difference(a, b):
    return abs(a[0] * a[1] * a[2] - b[0] * b[1] * b[2])
