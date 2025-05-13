def multiply(a: float, b: float) -> float:
    return a * b
print("Example 1: ", multiply(4, 5))  
print("Example 2: ", multiply(1.5, 2.3))  

def even_or_odd(number: int) -> str:
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(4))  
print(even_or_odd(7)) 


