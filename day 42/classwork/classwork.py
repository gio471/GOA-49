# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
def is_isogram(string): 
    return len(set(string.lower())) == len(string)

# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())


# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python
def find_short(s):
    return min(len(x) for x in s.split())