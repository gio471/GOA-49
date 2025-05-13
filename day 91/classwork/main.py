def fake_bin(x):
    result = ""
    for digit in x:
        num = int(digit)
        if num < 5:
            result += "0"
        else:
            result += "1"
    return result



def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000



def get_count(sentence):
    vowel = {"a","e","i","o","u"}
    count = 0
    for i in sentence:
        if i in vowel:
            count += 1
    return count