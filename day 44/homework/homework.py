#  https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

#  https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python
def openOrSenior(data):
    # Hmmm.. Where to start?
    ret = []
    for datum in data:
        age, handicap = datum
        if age >= 55 and handicap > 7:
            ret.append('Senior')
        else:
            ret.append('Open')
    return ret

# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python
def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1

# https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python
def nb_year(p0, percent, aug, p):
    # p0 - начальное население, percent - процент добавления, aug - пребывающие каждый год, p - что нужно превзойти
    per = percent/100
    pn = p0
    i = 0
    while pn < p:
        i = i + 1
        pn = int(pn + pn * per + aug)
        
    return i

# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))


