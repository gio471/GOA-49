# https://www.codewars.com/kata/55b42574ff091733d900002f/train/python
def friend(x):
    #Code
    names = []
    for name in x:
        if len(name) == 4:
            names.append(name)
    return names

# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python
def maskify(cc):
    return '{message:#>{fill}}'.format(message=cc[-4:], fill=len(cc))


#  https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python
def add_binary(a,b):
    return bin(a+b)[2:]

# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

# https://www.codewars.com/kata/56606694ec01347ce800001b/train/python
def is_triangle(a, b, c):
    return 2 * max(a, b, c) < a + b + c