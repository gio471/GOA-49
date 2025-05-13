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




