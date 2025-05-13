# https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
def square_digits(num):
    num = str(num)
    ans = ''
    for i in num:
        ans += str(int(i)**2)
    return int(ans) 


# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
def filter_list(l):
    new_list =[]
    for x in l:
        if type(x) != str:
            new_list.append(x)
    return new_list 


# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))


# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
def is_square(n):    
    return n == (n ** 0.5) ** 2


# https://www.codewars.com/kata/56747fd5cb988479af000028/train/python
def get_middle(s):
    while len(s) > 2:
        s = s[1:-1]
    return s


