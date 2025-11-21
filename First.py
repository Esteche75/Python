class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Welcome {self.name}. You are {self.age} år gammal.")

def create_person():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    return Person(name, age)


user = create_person()

user.greet() 
