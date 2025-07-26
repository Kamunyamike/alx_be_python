class Shape:
    def calculate_area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def calculate_area(self):
        return self.x * self.y



rectangle = Rectangle(5,9)
print(f"The area of the rectangle is: {rectangle.calculate_area()}")