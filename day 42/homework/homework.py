#  https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
def solution(string, ending):
    return string.endswith(ending)

# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
def accum(s):
    counter = 0
    output = ""
    for letter in s:
        output += letter.upper() + letter.lower() * counter + '-'
        counter += 1
    return output[:-1]


# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python
def DNA_strand(dna):
    return dna.translate(dna.maketrans("ATCG", "TAGC"))

# https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
def get_sum(a,b):
    return sum([x for x in range(min(a,b),max(a,b)+1)])