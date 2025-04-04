class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining balance: ₹{self.__balance}")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Current balance for {self.owner}: ₹{self.__balance}")

account = BankAccount("Hemachandra", 1000)

account.deposit(500)
account.withdraw(200)
account.check_balance()

#print(account.__balance) # Will raise an AttributeError

print(account._BankAccount__balance)  # Output: 1300

