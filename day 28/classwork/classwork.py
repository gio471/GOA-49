# https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0
def remove_char(s):
    return s[1:-1]
print(remove_char("eloquent")) 
print(remove_char("country"))   
print(remove_char("person"))   
print(remove_char("place")) 


# https://www.codewars.com/kata/515e271a311df0350d00000f
def square_sum(numbers):
    result = []
    for sqr in numbers:
        result.append(sqr ** 2)
    return sum(result)

#  https://www.codewars.com/kata/55a2d7ebe362935a210000b2
def findSmallestInt(arr):
    return min(arr)


#  https://www.codewars.com/kata/544675c6f971f7399a000e79
def string_to_number(s):
    return int(s)


# https://www.codewars.com/kata/55d24f55d7dd296eb9000030
def summation(num):
    return sum(range(1,num+1))


#  https://www.codewars.com/kata/523b4ff7adca849afe000035
def greet():
    return "hello world!"