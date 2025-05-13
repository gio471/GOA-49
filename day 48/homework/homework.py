# https://www.codewars.com/kata/55cb632c1a5d7b3ad0000145/train/python

def hoop_count(n):
    if n >= 10:
        return "Great, now move on to tricks"
    else:
        return "Keep at it until you get it"


# https://www.codewars.com/kata/55fab1ffda3e2e44f00000c6/train/python
def cockroach_speed(s):
    return int(s*27.778)


# https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/train/python
def switch_it_up(number):
    if number == 0:
        return "Zero"
    elif number == 1:
        return "One"
    elif number == 2:
        return "Two"
    elif number == 3:
        return "Three"
    elif number == 4:
        return "Four"
    elif number == 5:
        return "Five"
    elif number == 6:
        return "Six"
    elif number == 7:
        return "Seven"
    elif number == 8:
        return "Eight"
    else:
        return "Nine"
    


# https://www.codewars.com/kata/523b623152af8a30c6000027/train/python
def square(n):
    return n**2



# https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/python
def remove_every_other(my_list):
    list1 = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            list1.append(my_list[i])
    return list1