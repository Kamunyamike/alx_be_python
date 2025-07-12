class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def student_details(self):
        student = f"{self.name}, {self.age}"
        return student
mike = Student("Mike", 25)
john = Student("John", 20)
print(f"{mike.student_details()}")
print(f"{john.student_details()}")