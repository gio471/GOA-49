# list:
# როცა საჭიროა ელემენტების დინამიური კოლექცია, რომელშიც დუბლიკატები
#  ნებადართულია და უნდა შევინახოთ ელემენტების რიგი.
# tuple:
# როცა მონაცემების უცვლელობაა მნიშვნელოვანი და საჭიროა ინდექსირებული წვდომა.
# set:
# როცა მნიშვნელოვანია ელემენტების უნიკალურობა და სწრაფი ძიება.



# https://www.codewars.com/kata/55f73be6e12baaa5900000d4/train/python
def goals(*a):
    return sum(a)


# https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python
def double_char(s):
    res = ''
    for i in s:
        res += i*2
    return res


#  https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1/train/python
def get_age(age):
    return int(age[0])


