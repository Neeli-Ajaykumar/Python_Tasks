""" Payment System (Runtime Polymorphism) 
An online store supports multiple payment methods: CreditCard, UPI, and 
NetBanking. Create a base class Payment with a method process_payment() and 
override it in each payment type."""

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        print("Processing payment of", self.amount)

class Creditcard(Payment):
    def process_payment(self):
        print("Payment of", self.amount, " through Credit card")    

class UPI(Payment):
    def process_payment(self):
        print("Payment of", self.amount, " through UPI")

class NetBanking(Payment):
    def process_payment(self):
        print("Payment of", self.amount, " through Net Banking")

payments = [Creditcard(1000), UPI(2000), NetBanking(30000)]

for method in payments:
    method.process_payment()
