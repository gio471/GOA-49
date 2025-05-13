# https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python
def area_or_perimeter(l , w):
    if l == w:
        tot = l * w
    else:
        tot = l * 2 + w * 2
    return tot


# https://www.codewars.com/kata/5a023c426975981341000014/train/python
def other_angle(a,b):
    return 180 - a - b


# https://www.codewars.com/kata/568dcc3c7f12767a62000038/train/python
def set_alarm(employed, vacation):
    if employed and vacation is False:
        return True
    else:
        return False
    

# https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python
def sum_mix(arr):
    somme = 0
    for i in arr:
        somme += int(i)
    return somme


#  https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)