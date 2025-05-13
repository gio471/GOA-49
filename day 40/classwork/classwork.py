# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
def getCount(s):
    return sum(c in 'aeiou' for c in s)

#  https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s


# https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
def square_digits(num):
    num = str(num)
    ans = ''
    for i in num:
        ans += str(int(i)**2)
    return int(ans)


