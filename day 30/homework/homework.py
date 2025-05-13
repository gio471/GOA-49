# https://www.codewars.com/kata/555086d53eac039a2a000083/train/python
def lovefunc( flower1, flower2 ):
    return (flower1 + flower2) % 2 == 1


# https://www.codewars.com/kata/53dc54212259ed3d4f00071c/train/python
def sum_array(a: list) -> int:
    return sum(a)


#  https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd/train/python
def paperwork(n, m):
    return max(n, 0)*max(m, 0)


# https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/train/python
def past(h, m, s):
    return (3600*h + 60*m + s) * 1000


# https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7/train/python
def make_upper_case(s: str) -> str:
    return s.upper()



def manual_replace(text, old, new):
    result = ""
    i = 0
    while i < len(text):
        if text[i:i+len(old)] == old:
            result += new
            i += len(old)  
        else:
            result += text[i]
            i += 1
    return result


def manual_len(s):
    count = 0
    for _ in s:
        count += 1
    return count
