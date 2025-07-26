class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Hello {self.name}, you are {self.age} years old.")
    def __del__(self):
        print(f"Goodbye {self.name}")
        
person = Person("Mike", 25)
person