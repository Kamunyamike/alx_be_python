class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price:float, quantity = 0):
        #Ran validations to receive attributes
        assert price >= 0, f"The price of the items can only be greater than or equal to zero."
        assert quantity >= 0, f"The quantity should only be greater than or equal to zero."
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        # Assign class characteristics to all
        Item.all.append(self)
    #A method to calculate price
    def calculate_total_price(self):
       return self.price * self.quantity
    # A method to calculate discount
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"        

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)


print(Item.__dict__)
print(item1.__dict__)

item2.apply_discount()
print(f"The discounted value for the {item2.name} is {item2.price}")

item1.apply_discount()
print(f"The discounted value for a {item1.name} is  {item1.price}")

item6 = Item("Car", 100000, 2)
item6.pay_rate = 0.95
item6.apply_discount()
print(f"The discounted value for a {item6.name} is {item6.price}")

print(Item.all)