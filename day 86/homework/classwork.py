# აბსტრაქტული კლასი არის კლასი, რომელიც არ შეიძლება იყოს ინსტანცირებული პირდაპირ და გამოიყენება მხოლოდ მემკვიდრეობითობისთვის


# პოლიმორფიზმი ნიშნავს "ბევრ ფორმას" და OOP-ში ეს ნიშნავს ობიექტების უნარს, მიიღონ მრავალი ფორმა ან რეალიზება.


# აგრეგაცია არის სპეციალური ტიპის ასოციაცია, რომელიც წარმოადგენს "მთლიანი-ნაწილის" ურთიერთობას. 


from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} is eating.")


class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")

if __name__ == "__main__":
    my_dog = Dog("Buddy")
    my_cat = Cat("Whiskers")
    
    my_dog.make_sound()  
    my_cat.make_sound()  
    
    my_dog.eat()  



class Shape:
    def draw(self):
        print("Drawing a shape")
    
    def draw_with_color(self, color):
        print(f"Drawing a shape with color: {color}")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

if __name__ == "__main__":
    shape1 = Circle()
    shape2 = Rectangle()
    
    shape1.draw()  
    shape2.draw()  
    
    shape3 = Shape()
    shape3.draw()               
    shape3.draw_with_color("red")  





class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
    
    def start(self):
        print(f"{self.engine_type} engine started")


class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  
    
    def start(self):
        print(f"{self.model}: ", end="")
        self.engine.start()

if __name__ == "__main__":

    v8 = Engine("V8")
    electric = Engine("Electric")
    

    car1 = Car("Ford Mustang", v8)
    car2 = Car("Tesla Model S", electric)
    
    car1.start()  
    car2.start()  
    

    v8.start()  