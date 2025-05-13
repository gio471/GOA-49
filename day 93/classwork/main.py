class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Woof woof!")



class User:
    user_count = 0  
    
    def __init__(self):
        User.user_count += 1  
    
    @staticmethod
    def get_user_count():
        return User.user_count