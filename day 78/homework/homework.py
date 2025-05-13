# 1)https://www.codewars.com/kata/5266876b8f4bf2da9b000362:

def likes(names):

    if len(names) == 0:
        return "no one likes this"

    elif len(names) == 1:
        return f"{names[0]} likes this"

    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"

    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"

    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


# 2)https://www.codewars.com/kata/5552101f47fc5178b1000050:

def dig_pow(n, p):
    digits = [int(d) for d in str(n)] 
    total = 0
    for i, digit in enumerate(digits):
        total += digit ** (p + i)
    if total % n == 0:
        return total // n
    else:
        return -1

# 3)https://www.codewars.com/kata/64bd02fed4faa40058c0b053:

def matrix_div(result, factor, position):
    k = len(factor)
    if position == 0:

        A = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(k):
            for j in range(k):
                for m in range(k):
                    A[i][m] = result[i][j][m] // factor[m][j]
        return A
    else:

        B = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(k):
            for j in range(k):
                for m in range(k):
                    B[m][j] = result[i][j][m] // factor[i][m]
        return B

# 4)https://www.codewars.com/kata/5b4e779c578c6a898e0005c5:

def draw_stairs(n):
    stairs = []
    for i in range(n):
        stair = " " * i + "I"
        stairs.append(stair)
        
    return "\n".join(stairs)

# 5)https://www.codewars.com/kata/5977618080ef220766000022 

def usdcny(usd):
    conversion_rate = 6.75
    cny = usd * conversion_rate
    return f"{cny:.2f} Chinese Yuan"