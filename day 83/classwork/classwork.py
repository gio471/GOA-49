# 1) შექმენით car class, მიეცით 4 ატრიბუტი და შეუქმენით 2 ფუნქცია class'ში. ამ class'ისგან შექმენით 3 ობიექტი და სამივეზე გატესტეთ ყვლა ატრიბუტის გამოტანა და მეთოდები.


class Car:
    def __init__(self,color,year,brand,horse_power):
        self.color = color
        self.year = year
        self.brand = brand
        self.horse_power = horse_power

    def drive(self):
        print(f"you are driving {self.color} {self.brand}")

    def stop(self):
        print("you stopped car")

car1 = Car("green","2000","bmw",20650)
car2 = Car("black","2032","mercedes",20040)
car3 = Car("white","2021","ferrari",2012)


print(car1.drive())
print(car2.drive())
print(car3.drive())

print(car1.stop())
print(car2.stop())
print(car3.stop())




# 2) შექმენით person class, მიეცით 3 ატრიბუტი და შეუქმენით 2 ფუნქცია class'ში.  ამ class'ისგან შექმენით რამდენიმე ობიექტი და პირველ ორზე გატესტეთ ყვლა ატრიბუტის გამოტანა და მეთოდები. ასევე შექმენით დამატებითი კლასის ცვლადი რომელიც დათვლის რამდენი ადამიანია ჯამში.

class Person:

    human = 0

    def __init__(self,color,height,hair_color):
        self.color = color
        self.height = height
        self.hair_color = hair_color

    def race(self):
        print(f"you are {self.color}")

    def size(self):
        print(f"your height is {self.height}")

Person.human += 1

Person1 = Person("black",1557,"green")
Person2 = Person("white",1537,"red")
Person3 = Person("yellow",1527,"blue")

print(Person1.race())
print(Person2.race())

print(Person1.size())
print(Person2.size())
                                                                    
print(Person.human)




# Dunder method  არის სპეციალური მეთოდი პითონში, რომელიც ორმაგი ქვედა ხაზით  იწყება და მთავრდება. 
# Instance Variables  არის ცვლადები, რომლებიც განსაზღვრულია კლასის კონკრეტული ობიექტისთვის და მათი მნიშვნელობა უნიკალურია თითოეული ობიექტისთვის
# Class Variables არის ცვლადები, რომლებიც განსაზღვრულია კლასის დონეზე და ერთნაირია ყველა ეგზემპლარისთვის.
# Blueprint  პროგრამირებაში აღნიშნავს კლასს, რომელიც განსაზღვრავს ობიექტების სტრუქტურას და ქევას
