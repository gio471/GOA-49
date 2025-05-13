#  https://www.codewars.com/kata/5fc7caa854783c002196f2cb/train/python:
def speedify(st):
    res = {}

    for i, x in enumerate(st):

        shift = ord(x) - ord('A')
        new_pos = i + shift

        res[new_pos] = x

    if not res:
        return ""
    max_pos = max(res.keys())

    result = [' '] * (max_pos + 1)
    for pos, char in res.items():
        result[pos] = char

    return ''.join(result)