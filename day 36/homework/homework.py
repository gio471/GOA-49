# https://www.codewars.com/kata/568d0dd208ee69389d000016
def rental_car_cost(d):
    discount = 0
    if d >= 7:
        discount = 50
    elif d >= 3:
        discount = 20
    return d * 40 - discount


# https://www.codewars.com/kata/5ce9c1000bab0b001134f5af
def quarter_of(month):
    
    if month in range(1, 4):
        return 1
    elif month in range(4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    elif month in range(10, 13):
        return 4
    

# https://www.codewars.com/kata/57a0885cbb9944e24c00008e
def remove_exclamation_marks(s):
    return s.replace('!', '')


# https://www.codewars.com/kata/5bb904724c47249b10000131
def points(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0]>res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count


# https://www.codewars.com/kata/58261acb22be6e2ed800003a
def get_volume_of_cuboid(length, width, height):
    return length * width *height





def is_in(element, collection):
    for item in collection:
        if item == element:
            return True
    return False
print(is_in(3, [1, 2, 3, 4]))  
print(is_in('a', 'banana'))    
print(is_in(5, [1, 2, 3, 4]))  