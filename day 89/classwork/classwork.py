# კომპოზიცია არის ურთიერთობა ობიექტებს შორის, სადაც ერთი ობიექტი  აკონტროლებს მეორე ობიექტის.


# Instance მეთოდი: იღებს პარამეტრად self,იძახება ობიექტის მეშვეობით.
# Class მეთოდი: იღებს პარამეტრად cls,გამოიყენება @classmethod.
# Static მეთოდი: გამოიყენება @staticmethod დეკორატორით,მოქმედებს როგორც ჩვეულებრივი ფუნქცია, მაგრამ კლასის ფარგლებშია.


class MyClass:
    class_attr = "Class Attribute"

    def __init__(self, value):
        self.instance_attr = value

    def instance_method(self):
        print(f"Instance attr: {self.instance_attr}")

    @classmethod
    def class_method(cls):
        print(f"Class attr: {cls.class_attr}")

    @staticmethod
    def static_method():
        print("This is a static method")


obj = MyClass("Instance Value")
obj.instance_method()  
MyClass.class_method()
MyClass.static_method()  





# Multilevel Inheritance: კლასი მემკვიდრეობით იღებს სხვა კლასს, რომელიც მემკვიდრეობით ღებულობს მესამე კლასს.

# Multiple Inheritance: კლასი ერთდროულად მემკვიდრეობით იღებს რამდენიმე კლასს.



# Data Hiding არის მონაცემებს გარე სამყაროსგან დავამალვა და მათზე წვდომა მხოლოდ შემქმნელებს აქვთ.
# როცა გვინდა მომხმარებლის ინფორმაციის დამალვა დეტალების დამალვა

class Secret:
    def __init__(self):
        self.__password = "1234"  
    
    def პაროლის_შემოწმება(self, submit):
        return submit == self.__password

S = Secret()

print(S.checking_password("0000"))  
print(S.checking_password("1234"))  