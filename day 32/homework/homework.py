#  https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python
def find_average(nums):
    if len(nums) == 0:
        return 0
    return sum(nums) / len(nums)


# https://www.codewars.com/kata/53dc23c68a0c93699800041d/train/python
def smash(words):
    return ' '.join(words)


#  https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python
def grow(arr):
	product = 1
	for i in arr:
		product *= i
	return product


# https://www.codewars.com/kata/59ca8246d751df55cc00014c/train/python
def hero(bullets, dragons):
    return dragons <= bullets / 2


# https://www.codewars.com/kata/5601409514fc93442500010b/train/python
def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)



def manual_find(text, substring):
  
    if not substring:
        return 0
    
    for i in range(len(text) - len(substring) + 1):
        if text[i:i+len(substring)] == substring:
            return i
    return -1
print(manual_find("hello world", "world"))  
print(manual_find("hello world", "python")) 
print(manual_find("hello world", ""))       



def manual_swapcase(text):
    result = []
    
    for char in text:
        if char.islower():  
            result.append(char.upper())  
        elif char.isupper():  
            result.append(char.lower())  
        else:
            result.append(char)  
    
    return ''.join(result)
print(manual_swapcase("Hello World!"))  
print(manual_swapcase("Python 123"))    
print(manual_swapcase("This Is A Test"))  



