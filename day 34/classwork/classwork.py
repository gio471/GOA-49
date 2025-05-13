# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
def count_positives_sum_negatives(arr):
    if not arr: 
        return []
    
    count_positives = sum(1 for x in arr if x > 0)  
    sum_negatives = sum(x for x in arr if x < 0)   
    return [count_positives, sum_negatives]
example = [1, 2, -1, -2, -3, 4]
result = count_positives_sum_negatives(example)
print(result)  


#  https://www.codewars.com/kata/5556282156230d0e5e000089/train/python
def dna_to_rna(dna):
    return dna.replace("T", "U")


# https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python
def zeroFuel(a, b, c):
    return b * c >= a


# https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python
def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    elif bmi > 30:
        return "Obese"
    

# https://www.codewars.com/kata/577a98a6ae28071780000989/train/python
def minimum(arr):
    return min(arr)
def maximum(arr):
    return max(arr)