# 1) შექმენით Motorcycle class'ი, 4 attribute'ით და 1 class variable'ით. class variable'მა უნდა დათვალოს რამდენი მოტოციკლეტი გაკეთდა, დანარჩენი თქვენ მოიფიქრეთ, ატრიბუტები რა იქნება და ა.შ
# class Motorcycle:
#     total_motorcycles = 0
    
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         Motorcycle.total_motorcycles += 1
    
#     def display_info(self):
#         print(f"{self.brand} {self.model} ({self.year})motorcycle")
#     def get_total_count():
#         return Motorcycle.total_motorcycles



# bike1 = Motorcycle("Harley-Davidson", "Sportster", 2022)
# bike2 = Motorcycle("Honda", "CBR600RR", 2021)

# bike1.display_info()  
# bike2.display_info()  




class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name} eats...")
    
    def sleep(self):
        print(f"{self.name} is sleaping...")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} sounds: WOF-WOF!")
    
    def fetch(self):
        print(f"{self.name} searchinf for ball")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def meow(self):
        print(f"{self.name} sound: MEOW-MEOW!")
    
    def climb(self):
        print(f"{self.name} climb on a tree")


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan
    
    def fly(self):
        print(f"{self.name} flyes with {self.wingspan}cm wings")
    
    def sing(self):
        print(f"{self.name} sings beautyfly")


dog = Dog("billi", 3, "cane corso")
cat = Cat("jek", 2, "black")
bird = Bird("birdy", 1, 30)

dog.eat()  
dog.bark()  
cat.sleep()  
cat.climb()  
bird.fly()  




# Inheritance საშუალებას გვაძლევს შევქმნათ ახალი კლასი (child class) რომელიც იღებს ატრიბუტებსა და მეთოდებს მშობელი კლასიდან.
# Inheritance გვჭირდება მაშინ როცა გვაქვს მრავალი კლასი რომლებსაც აქვთ საერთო ფუნქციონალი
#Multiple instances of the same app refer to running several copies of the same application simultaneously on a device or system. This can occur in various contexts.
