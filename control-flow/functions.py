def greet(name):
    print(f"Hi,{name}. how are you doing?")

greet(name = "John")
greet(name = "Mike")

def area(length, width):
    return length * width

print(f"The area of the rectangle is: {area(5,6)}")

def even(number):
    if number%2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
even(14)