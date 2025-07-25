class Item:
    def __init__(self, name, price, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    #
    def calculate_total_price(self, price, quantity):
       return self.price * self.quantity

item1 = Item()
item1.name = "Phone"
item1.price = 50
item1.quantity = 10

print(item1.calculate_total_price(item1.price, item1.quantity))
print(f"The total price for {item1.name} of quantity {item1.quantity} is : {item1.calculate_total_price(item1.price, item1.quantity)}")


item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 4
print(f"The total price for {item2.name} of the quantity {item2.quantity} is {item2.calculate_total_price(item2.price, item2.quantity)}")

