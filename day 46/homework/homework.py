#  https://www.codewars.com/kata/55cbc3586671f6aa070000fb/train/python
def check_for_factor(base, factor):
    return base % factor == 0



def remove_duplicates_preserve_order(input_string):
    seen = set()
    result = []
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)
string_with_duplicates = "hello world"
result = remove_duplicates_preserve_order(string_with_duplicates)
print(result)  

# https://www.codewars.com/kata/5aa736a455f906981800360d/train/python
def feast(beast, dish):
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    else:
        return False 
    

#  https://www.codewars.com/kata/5a2be17aee1aaefe2a000151/train/python
def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)


#  https://www.codewars.com/kata/563e320cee5dddcf77000158/train/python
def get_average(marks):
    return sum(marks) // len(marks)


# https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python
def reverseWords(str):
    return " ".join(str.split(" ")[::-1])
