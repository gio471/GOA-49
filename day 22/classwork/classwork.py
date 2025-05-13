def goodbye_world():
    print("goodbye world")
goodbye_world()

def goodbye_name(name):
    print(f"Goodbye, {name}!")
goodbye_name("giorgi")  # მაგალითად

def add_two_numbers(a, b):
    print(a + b)
add_two_numbers(6, 7)

def get_first_three(numbers):
    return numbers[:3]
numbers = [1, 2, 3, 4, 5]
result = get_first_three(numbers)
print(result)