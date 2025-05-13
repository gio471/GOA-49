# https://www.codewars.com/kata/526c7363236867513f0005ca:

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# https://www.codewars.com/kata/559ac78160f0be07c200005a:

def name_shuffler(str_):
    names = str_.split()  
    return f"{names[1]} {names[0]}"


# https://www.codewars.com/kata/56b0ff16d4aa33e5bb00008e:

def shorten_to_date(long_date):
    return long_date.split(',')[0]

# https://www.codewars.com/kata/529eef7a9194e0cbc1000255:

def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())


# https://www.codewars.com/kata/52fb87703c1351ebd200081f:

def what_century(year):
    year = int(year)

    century = (year - 1) // 100 + 1
    
    if 10 <= century % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(century % 10, "th")
    return f"{century}{suffix}"