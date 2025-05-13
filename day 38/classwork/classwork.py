numbers = [x for x in range(1, 101)]
print(numbers)
[1, 2, 3, 4, 5, ..., 100]


numbers = [x for x in range(1, 101, 2)]
print(numbers)
[1, 3, 5, 7, 9, ..., 99]


names = ["Anna", "John", "Maria", "Alice", "Bob"]  # ორიგინალური სია
filtered_names = [f"#{name}" for name in names if "a" not in name.lower()]
print(filtered_names)
['#John', '#Bob']


#  https://www.codewars.com/kata/55225023e1be1ec8bc000390
def greet(name):
    return "Hello, my love!" if name == 'Johnny' else "Hello, {name}!".format(name=name)


# https://www.codewars.com/kata/58649884a1659ed6cb000072
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "This is not a traffic light color."
    

