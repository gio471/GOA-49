word1 = "goabest"
# try:
#     print(wird2)    -  error
# except:
#     print("there is name error")
list1 = [1,2,3,4,5,6,7,8,9]
try:
    print(list1[15])
except:
    print("there is index error")
str1 = "1234ggbyuid78t5"
try:
    print(int(str1))
except:
    print("there is value error")





def summination(list1):
    count = 0
    for i in list1:
        count += int(i)
    return count



#https://www.codewars.com/kata/5865918c6b569962950002a1/train/python
def str_count(strng, letter):
    count = 0
    for i in strng:
        if letter == i:
            count += 1
    return count

#https://www.codewars.com/kata/555a67db74814aa4ee0001b5/train/python
def is_even(n): 
    if n %  2 == 0:
        return True
    elif n == float():
        return False
    else:
        return False