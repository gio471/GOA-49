# https://www.codewars.com/kata/58ca658cc0d6401f2700045f/train/python:

def find_multiples(integer, limit):
    return [i for i in range(integer, limit + 1, integer)]


# https://www.codewars.com/kata/50ee6b0bdeab583673000025/train/python:

a = "code"
b = "wa.rs"
name = a + b

# https://www.codewars.com/kata/55c28f7304e3eaebef0000da/train/python:

def create_array(n):
    res=[]
    i=1
    while i<=n: 
      res +=[i]
      i = i+1
    return res


# https://www.codewars.com/kata/56fa3c5ce4d45d2a52001b3c/train/python:

def xor(a, b):
    return a != b


# https://www.codewars.com/kata/574b3b1599d8f897470018f6/train/python:

def get_real_floor(n):
    if n < 0:
        return n  
    elif n == 0:
        return 0  
    elif 1 <= n <= 12:
        return n - 1  
    else:
        return n - 2  
    
# https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/train/python:

def goose_filter(birds):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    return [bird for bird in birds if bird not in geese]


# https://www.codewars.com/kata/55edaba99da3a9c84000003b/train/python:

def divisible_by(numbers, divisor):
    div_by = []
    for num in numbers:
        if num % divisor == 0:
            div_by.append(num)
    return div_by

# https://www.codewars.com/kata/559ac78160f0be07c200005a/train/python:

def name_shuffler(str_):
    names = str_.split()  
    return f"{names[1]} {names[0]}"

# https://www.codewars.com/kata/56b29582461215098d00000f/train/python:

def pipe_fix(nums):
    return list(range(nums[0], nums[-1] + 1))


# https://www.codewars.com/kata/57202aefe8d6c514300001fd/train/python:

def sale_hotdogs( _n ):
    if _n < 5:
        return _n * 100
    elif _n >= 10:
        return _n * 90
    else:
        return _n * 95