# https://www.codewars.com/kata/577ff15ad648a14b780000e7/train/python:

def greet(language):

    greetings_db = {
        "english": "Welcome",
        "czech": "Vitejte",
        "danish": "Velkomst",
        "dutch": "Welkom",
        "estonian": "Tere tulemast",
        "finnish": "Tervetuloa",
        "flemish": "Welgekomen",
        "french": "Bienvenue",
        "german": "Willkommen",
        "irish": "Failte",
        "italian": "Benvenuto",
        "latvian": "Gaidits",
        "lithuanian": "Laukiamas",
        "polish": "Witamy",
        "spanish": "Bienvenido",
        "swedish": "Valkommen",
        "welsh": "Croeso"
    }

    if isinstance(language, str):
        return greetings_db.get(language.lower(), "Welcome")
    else:

        return "Welcome"

# https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/python:

def two_sort(array):
    sorted_array = sorted(array)
    first_value = sorted_array[0]
    result = '***'.join(first_value)
    
    return result

# https://www.codewars.com/kata/56170e844da7c6f647000063/train/python:

def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"


# https://www.codewars.com/kata/50654ddff44f800200000007/train/python:

def solution(a, b):

    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b



# https://www.codewars.com/kata/56f699cd9400f5b7d8000b55/train/python:
def fix_the_meerkat(arr):
    return [arr[2], arr[1], arr[0]]