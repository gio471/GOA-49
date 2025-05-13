# https://www.codewars.com/kata/598ee7b6ec6cb90dd6000061:

def count_repeats(txt):
    if not txt:
        return 0
    
    count = 0
    previous_char = txt[0]
    
    for current_char in txt[1:]:
        if current_char == previous_char:
            count += 1
        else:
            previous_char = current_char
    
    return count

# https://www.codewars.com/kata/576757b1df89ecf5bd00073b:

def tower_builder(n_floors):
    tower = []
    max_width = 2 * n_floors - 1 
    
    for floor in range(1, n_floors + 1):
        stars = 2 * floor - 1
        spaces = (max_width - stars) // 2
        floor_str = " " * spaces + "*" * stars + " " * spaces
        tower.append(floor_str)
    
    return tower

# https://www.codewars.com/kata/51f41fe7e8f176e70d0002b9:

def sortme(words):
    return sorted(words, key=lambda x: x.lower())