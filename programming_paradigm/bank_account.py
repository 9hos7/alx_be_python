class BankAccount:
    def __init__(self, initial_amount=0):
        self.account_balance = initial_amount

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance > amount:
            self.account_balance -= amount
        else:
            print("insufficient funds.")

    def display_balance(self):
        print(f'Current Balance: ${self.account_balance}')