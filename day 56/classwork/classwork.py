listg = [33,45,65,77,21,12]
listg1 = list(filter(lambda x:x >= 40,listg))
print(listg1)


listg2 = list(map(lambda x:x ** 2,listg))
print(listg2)


listn= ["fg","vhjba","fvb","vghvfkwa","hjdfdiea"]
listn1 = list(filter(lambda word:word.endswith("a"),listn))
print(listn1)




# https://www.codewars.com/kata/515e188a311df01cba000003/train/python:

def get_planet_name(id):
    # This doesn't work; Fix it!
    name=""
    match id:
        case 1: name = "Mercury"
        case 2: name = "Venus"
        case 3: name = "Earth"
        case 4: name = "Mars"
        case 5: name = "Jupiter"
        case 6: name = "Saturn"
        case 7: name = "Uranus"  
        case 8: name = "Neptune"
    return name

# https://www.codewars.com/kata/563a631f7cbbc236cf0000c2/train/python:

def move(position, roll):
    return position + (2 * roll)

# https://www.codewars.com/kata/5875b200d520904a04000003/train/python:

def enough(cap, on, wait):
    available_space = cap - on  
    return max(0, wait - available_space)

# https://www.codewars.com/kata/55ecd718f46fba02e5000029/train/python:

def between(a, b):
    result = []
    while a <= b:
        result.append(a)
        a += 1
    return result

# https://www.codewars.com/kata/5625618b1fe21ab49f00001f/train/python:
def say_hello(name):
    return f"Hello, {name}"