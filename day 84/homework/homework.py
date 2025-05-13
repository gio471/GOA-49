# Abstract methods are a fundamental concept in object-oriented programming (OOP) that enable abstraction - one of the core OOP principles. Here's a comprehensive explanation:


class Worker:
    def __init__(self, name):
        self.name = name  

    def work(self):
        print(f"{self.name} is working")

class Student:
    def __init__(self, id):
        self.id = id  

    def study(self): 
        print(f"Student {self.id} is studying")

class WorkingStudent(Worker, Student):
    def __init__(self, name, id):
        Worker.__init__(self, name)  
        Student.__init__(self, id)   

ws = WorkingStudent("Alice", "S123")
ws.work()    
ws.study()  



class Vehicle:
    def __init__(self, brand):
        self.brand = brand  
    def start(self): 
        print(f"{self.brand} engine started")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  
        self.model = model       
    def drive(self): 
        print(f"Driving {self.brand} {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)  
        self.battery = battery         
    def charge(self): print(f"Charging {self.battery}kWh battery")

tesla = ElectricCar("Tesla", "Model 3", 75)
tesla.start()   
tesla.drive()   
tesla.charge()  


class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  
        self.breed = breed
    
    def speak(self):
        parent_sound = super().speak()  
        print(f"{parent_sound} WOOF-WOOF")


my_dog = Dog("Billi", "Came Corso")
print(my_dog.name)    
print(my_dog.speak()) 