#https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
def solution(number):
    sum1 = 0
    for i in range(number):
        if i % 3 ==0 or i%5 == 0:
            sum1+=i
    return sum1