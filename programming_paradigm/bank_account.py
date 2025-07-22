class BankAccount:
    def __init__(self, initial_balance = 250.0):
        if not isinstance(initial_balance, (int,float)):
            raise TypeError("Initial balance must be a number.")
        if initial_balance < 0:
            raise ValueError("The Initial balance cannot be a negative.")
        self.account_balance = initial_balance
    def deposit(self, amount):
        if not isinstance(amount,(int,float)):
            print("Please enter a valid input for your deposits.")
            return False
        if amount < 0:
            print("The deposit cannot be a negative figure.")
            return False
        self.account_balance += amount
        
        return True
    def withdraw(self, amount):
        if not isinstance(amount, (int,float)):
            print("Please enter a valid input for withdrawal.")
            return False
        if amount < 0:
            print("You cannot withdraw a negative figure.")
        if self.account_balance >= amount:
            self.account_balance -+ amount
            return True
        else:
            return False
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")