# https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python:
def create_phone_number(n):
    n = "".join([str(i) for i in n])
    return f"({n[:3]}) {n[3:6]}-{n[6:]}"

# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python:

def likes(names):

    if len(names) == 0:
        return "no one likes this"

    elif len(names) == 1:
        return f"{names[0]} likes this"

    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"

    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"

    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python:

def find_it(seq):
    result = 0
    for num in seq:
        result ^= num  
    return result

# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python:
def move_zeros(lst):
    non_zeros = [num for num in lst if num != 0]
    zeros = lst.count(0)
    return non_zeros + [0] * zeros