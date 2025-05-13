# https://www.codewars.com/kata/5672a98bdbdd995fad00000f
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"


# https://www.codewars.com/kata/5545f109004975ea66000086
def is_divisible(n,x,y):
  
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False
    

# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077
def count_sheep(n):
    s = ""
    i = 1
    while i <= n:
        s += str(i)+" sheep..."
        i += 1
    return s


# https://www.codewars.com/kata/55cbd4ba903825f7970000f5
def get_grade(s1, s2, s3):
    m = (s1 + s2 + s3) / 3.0
    if 90 <= m <= 100:
        return 'A'
    elif 80 <= m < 90:
        return 'B'
    elif 70 <= m < 80:
        return 'C'
    elif 60 <= m < 70:
        return 'D'
    return "F"


#  https://www.codewars.com/kata/5772da22b89313a4d50012f7
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"