# https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python
def basic_op(operation: str, value1: int, value2: int) -> int:
    if operation == "+":
        return value1 + value2
    elif operation == "-":
        return value1 - value2
    elif operation == "*":
        return value1 * value2
    elif operation == "/":
        return value1 / value2
    

# https://www.codewars.com/kata/582cb0224e56e068d800003c/train/python
def litres(time: float) -> int:
    return int(time * 0.5)


# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python
def century(year: int) -> int:
    return (year + 99) // 100


# https://www.codewars.com/kata/57f781872e3d8ca2a000007e/train/python
def maps(a):
    return list(map(lambda x: x * 2, a))


# https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
def digitize(n):
    mylist = [int(i) for i in str(n)]
    mylist.reverse()
    return mylist