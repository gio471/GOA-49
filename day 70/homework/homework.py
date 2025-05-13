# https://www.codewars.com/kata/52fba2a9adcd10b34300094c:

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

# https://www.codewars.com/kata/54e6533c92449cc251001667:

def unique_in_order(sequence):
    result = []
    for i in range(len(sequence)):

        if not result or sequence[i] != result[-1]:
            result.append(sequence[i])
    
    return result

# https://www.codewars.com/kata/578553c3a1b8d5c40300037c:

def binary_array_to_number(arr):
    return int(''.join(map(str, arr)), 2)


# https://www.codewars.com/kata/5842df8ccbd22792a4000245:

def expanded_form(num):
    num_str = str(num)
    expanded = []
    length = len(num_str)
    
    for i, digit in enumerate(num_str):
        if digit != '0':
            expanded.append(digit + '0' * (length - i - 1))
    return ' + '.join(expanded)

# https://www.codewars.com/kata/515decfd9dcfc23bb6000006:

def is_valid_IP(strng):

    octets = strng.split('.')
    if len(octets) != 4:
        return False

    for octet in octets:
        if not octet.isdigit():
            return False
        if octet != "0" and octet.startswith("0"):
            return False
        if not (0 <= int(octet) <= 255):
            return False
    return True