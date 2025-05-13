# https://www.codewars.com/kata/5574835e3e404a0bed00001b/train/python:import math

import math

def get_participants(handshakes):
    if handshakes == 0:
        return 0
    discriminant = 1 + 8 * handshakes
    n = (1 + math.sqrt(discriminant)) / 2
    return math.ceil(n)


# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python:

def delete_nth(order, max_e):
    count = {}
    result = []
    for num in order:
        if num not in count:
            count[num] = 0
        if count[num] < max_e:
            result.append(num)
            count[num] += 1
    return result
# https://www.codewars.com/kata/58a66c208b88b2de660000c3/train/python:

def missing_values(seq):
    count = {}
    for num in seq:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    x = None
    y = None
    for num, cnt in count.items():
        if cnt == 1:
            x = num
        elif cnt == 2:
            y = num
    
    return x * x * y


# https://www.codewars.com/kata/56f253dd75e340ff670002ac/train/python:

def compose(s1, s2):
    lines1 = s1.split('\n')
    lines2 = s2.split('\n')
    n = len(lines1)
    strng = []
    
    for i in range(n):
        part1 = lines1[i][:i + 1]  
        part2 = lines2[n - 1 - i][:n - i] 
        strng.append(part1 + part2)
    
    return '\n'.join(strng)