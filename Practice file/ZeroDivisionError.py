x = int(input("Enter your numerator value: "))
y = int(input("Enter your denominator value: "))

def division(x,y):
    if y == 0:
        raise ZeroDivisionError("Division by Zero is not allowed.")
    return (x/y)
print(division(x,y))