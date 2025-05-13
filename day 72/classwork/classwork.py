# https://www.codewars.com/kata/58539230879867a8cd00011c/train/python:

def find_children(dancing_brigade):
    return ''.join( sorted(dancing_brigade, key=lambda l: (l.lower(),l)) )

# https://www.codewars.com/kata/5878520d52628a092f0002d0/train/python:

def string_transformer(s):
    swapped = s.swapcase()
    parts = []
    temp = ""
    for char in swapped:
        if char == " ":
            if temp:
                parts.append(temp)
                temp = ""
            parts.append(" ")
        else:
            temp += char
    if temp:
        parts.append(temp)
    parts.reverse()
    return "".join(parts)


# https://www.codewars.com/kata/5410c0e6a0e736cf5b000e69/train/python:

def hamming(a, b):
    distance = 0
    for char_a, char_b in zip(a, b):
        if char_a != char_b:
            distance += 1
    return distance
