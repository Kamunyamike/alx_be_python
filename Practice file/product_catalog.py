#Define a Product class with attributes like name, price, and quantity. 
#Implement a method to calculate the total value of products in stock.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def product_details(self):
        product = f"Name: {self.name}, Price: {self.price} * Quantity: {self.quantity}"
        return product
    def calculate_total_value(self):
        total_value = self.price * self.quantity
        return total_value
car = Product("Car", 1000000,2)
bike = Product("Bike", 9999, 12)
phone = Product("Phone", 20000, 2)
hoodie = Product("Hoodie", 1200, 12)
laptop = Product("Laptop", 45000, 8)

print(f"The details of the product is: {car.product_details()}")
print(f"The price of the product is: {car.calculate_total_value()}")

print(f"The details of the product is: {bike.product_details()}")
print(f"The price of that product is: {bike.calculate_total_value()}")

print(f"The details of the product is: {phone.product_details()}")
print(f"The price of the product is: {phone.calculate_total_value()}")

print(f"The details of the product is: {hoodie.product_details()}")
print(f"The price of the product is: {hoodie.calculate_total_value()}")

print(f"The details of the product is: {laptop.product_details()}")
print(f"The price of the product is: {laptop.calculate_total_value()}")