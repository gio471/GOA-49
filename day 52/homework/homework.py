sumstr1 = lambda str1,str2: str1+str2
print(sumstr1("gio","goa"))



sum1 = lambda num1,num2,num3: num1+num2+num3
print(sum1(5,4,3))



sumlst = lambda list5: sum(list5)
print(sumlst([1,2,3]))



counter = lambda str3,x:  str3.count(x)
print(counter("hellllo","l"))




def twice_as_old(dad_years_old, son_years_old):
    twice1 = son_years_old*2
    return abs(dad_years_old - twice1)



def move(position, roll):
    return position + (roll*2)



def get_planet_name(id):
    return {
         1: "Mercury",
         2: "Venus",
         3: "Earth",
         4: "Mars",
         5: "Jupiter",
         6: "Saturn",
         7: "Uranus"  ,
         8: "Neptune",
        }[id]


def enough(cap, on, wait):
    if wait - (cap-on) > 0:
        return  wait - (cap-on)
    else:
        return 0

def between(a,b):
    return list(range(a,b+1))

