# Level 84:
# 1) გააკეთეთ multiple და multilevel inheritanceის მაგალითი ზუსტად ისე როგორც კლასში გავაკეთეთ ოღონდ ადამიანებზე
# cheatsheet:
# ```
# Human

# Programmer(Human)
# Designer(Human)

# Goaprogrammer(Programmer)
# Goadesiner(Designer)

# Professional(Programmer, Designer)
# ```


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"I am {self.name}, {self.age} years old."

class Programmer(Human):
    def __init__(self, name, age, language):
        Human.__init__(self, name, age)
        self.language = language
    
    def code(self):
        return f"I code in {self.language}."

class Designer(Human):
    def __init__(self, name, age, tool):
        Human.__init__(self, name, age)
        self.tool = tool
    
    def design(self):
        return f"I design using {self.tool}."

class Goaprogrammer(Programmer):
    def __init__(self, name, age):
        Programmer.__init__(self, name, age)
    
    def special_skill(self):
        return "I teach in goa programming academy."

class Goadesigner(Designer):
    def __init__(self, name, age):
        Designer.__init__(self, name, age, "Adobe Illustrator")
    
    def special_skill(self):
        return "I make logos for goa."

class Professional(Programmer, Designer):
    def __init__(self, name, age, language, tool):
        Programmer.__init__(self, name, age, language)
        Designer.__init__(self, name, age, tool)
    
    def full_skills(self):
        return f"I am a professional who codes in {self.language} and designs using {self.tool}."

human = Professional("Giorgi", 30, "Python", "Figma")
print(human.introduce())  
print(human.code())       
print(human.design())     
print(human.full_skills()) 



# super() გამოიყენება მშობელი კლასის მეთოდებისა და ატრიბუტების გამოსაძახებლად შვილობილ კლასში. 
# super() გამოიძახებს მშობელი კლასის კონსტრუქტორს __init__-ის, რაც საშუალებას გვაძლევს, გადმოვიტანოთ მშობელი კლასის ატრიბუტები შვილობილ კლასში.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")  
        self.breed = breed  

    def make_sound(self):
        print("Bark")

dog1 = Dog("Billi", "Cane Corso")

print(dog1.name)       
print(dog1.species)    
print(dog1.breed)      
print(dog1.make_sound())  