def disemvowel(string_):
    vowels = "aeiouAEIOU"
    result = []
    for char in string_:
        if char not in vowels:
            result.append(char)
    return ''.join(result)



def square_digits(num):
    num_str = str(num)
    result_str = ""
    for digit in num_str:
        squared = int(digit) ** 2
        result_str += str(squared)
    return int(result_str)