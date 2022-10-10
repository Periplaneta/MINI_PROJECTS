class Account:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status
        self.balance = 0

    def balance(self):
        print(f"{self.name}, your current balance is ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name}, you just made a deposite of ${amount} and your current balance is ${self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"{self.name}, you just made a withdrawal of ${amount} and your current balance is ${self.balance}")


