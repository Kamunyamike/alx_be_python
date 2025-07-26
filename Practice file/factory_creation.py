gitclass Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def create_child(cls, name):
        return cls(name, 0)
    
    def __str__(self):
        return f"This is {self.name}, who is {self.age} years old."



adult = Person("John", 10)
child = Person.create_child("Kennedy")

print(adult)
print(child)