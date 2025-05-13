class Animal:
    def speak(self):
        """Base method for animal sounds"""
        print("Animal makes a sound")
    
    def __str__(self):
        return "Generic Animal"

class Dog(Animal):
    def speak(self):
        """Override to make dog-specific sound"""
        print("Woof woof!")
    
    def __str__(self):
        return "Dog"
    




class User:
    _user_count = 0  
    
    def __init__(self, username=None):
        """Initialize a new user, optionally with a username"""
        self.username = username
        User._user_count += 1
    
    @staticmethod
    def get_user_count():
        """Return the total number of users created"""
        return User._user_count
    
    @classmethod
    def reset_count(cls):
        """Reset the user counter (for testing purposes)"""
        cls._user_count = 0