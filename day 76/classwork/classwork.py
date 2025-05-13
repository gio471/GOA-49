#https://www.codewars.com/kata/526233aefd4764272800036f/solutions/python:
def matrix_addition(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for x in range(len(a[0])):
            row.append(a[i][x] + b[i][x])
        result.append(row)
    return result

#https://www.codewars.com/kata/5503013e34137eeeaa001648/train/python:
def diamond(n):
    if n % 2 == 0 or n <= 0:
        return None
    diamond_str = []
    for i in range(1, n + 1, 2):
        spaces = (n - i) // 2
        diamond_str.append(" " * spaces + "*" * i + "\n")
    for i in range(n - 2, 0, -2):
        spaces = (n - i) // 2
        diamond_str.append(" " * spaces + "*" * i + "\n")

    return "".join(diamond_str)

