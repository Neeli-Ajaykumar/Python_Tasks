"""Bank Account System (Class, Object, Constructor) 
A bank wants to manage customer accounts. Create a BankAccount class with a 
constructor to initialize account number and balance. Implement methods to deposit, 
withdraw, and display balance. """

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited amount is:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)
        print("----------------------")

account = BankAccount(40351866266, 10000)
account.display_balance()

account.deposit(5000)
account.display_balance()

account.withdraw(3000)
account.display_balance()

