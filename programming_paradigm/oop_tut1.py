import csv

class Item:
    pay_rate = 0.8
    all = []  # class-level list to store all instances

    def __init__(self, name: str, price: float, quantity=0):
        # Validations
        assert price >= 0, "Price must be non-negative."
        assert quantity >= 0, "Quantity must be non-negative."

        # Assign to self object
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

        # Add instance to the class-level list
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls, filename="items.csv"):
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header if present
            for row in reader:
                name, price, quantity = row
                cls(name, float(price), int(quantity))


def main():
    Item.instantiate_from_csv()
    print(Item.all)  # Show all Item instances

if __name__ == "__main__":
    main()
