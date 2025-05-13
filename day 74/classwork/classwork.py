# 1) https://www.codewars.com/kata/5574835e3e404a0bed00001b/train/python:

import math

def get_participants(handshakes):
    if handshakes == 0:
        return 0
    discriminant = 1 + 8 * handshakes
    n = (1 + math.sqrt(discriminant)) / 2
    return math.ceil(n)

# 2) https://www.codewars.com/kata/52761ee4cffbc69732000738/train/python:

def good_vs_evil(good, evil):
    good_worth = [1, 2, 3, 3, 4, 10]
    evil_worth = [1, 2, 2, 2, 3, 5, 10]

    good_counts = list(map(int, good.split()))
    evil_counts = list(map(int, evil.split()))
    
    good_total = sum(g_count * g_worth for g_count, g_worth in zip(good_counts, good_worth))
    evil_total = sum(e_count * e_worth for e_count, e_worth in zip(evil_counts, evil_worth))
    
    if good_total > evil_total:
        return "Battle Result: Good triumphs over Evil"
    elif evil_total > good_total:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"

# 3) https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python:

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