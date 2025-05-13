# https://www.codewars.com/kata/556196a6091a7e7f58000018/train/python:

def largest_pair_sum(numbers):
    max1 = max(numbers)  
    numbers.remove(max1)  
    max2 = max(numbers)  
    return max1 + max2

# https://www.codewars.com/kata/52fba2a9adcd10b34300094c/train/python:

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python:

def unique_in_order(sequence):
    result = []
    for i in range(len(sequence)):

        if not result or sequence[i] != result[-1]:
            result.append(sequence[i])
    
    return result
