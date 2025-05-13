# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python
def abbrev_name(name):
    parts = name.split()
    initials = parts[0][0].upper() + '.' + parts[1][0].upper()
    return initials
print(abbrev_name("Sam Harris"))  
print(abbrev_name("patrick feeney"))


# https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    print(are_you_playing_banjo("Ravi"))  
print(are_you_playing_banjo("Sam"))  
print(are_you_playing_banjo("robert"))  
print(are_you_playing_banjo("David")) 


#  https://www.codewars.com/kata/583710ccaa6717322c000105/train/python
def simple_multiplication(number):
    if number % 2 == 0: 
        return number * 8
    else:  
        return number * 9
print(simple_multiplication(4))   
print(simple_multiplication(7))   
print(simple_multiplication(10)) 
print(simple_multiplication(3))


# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python
def find_needle(haystack):
    for i, x in enumerate(haystack):
        if x == 'needle': 
            return 'found the needle at position %d' % i
        

#  https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python
def invert(l): return [-n for n in l]