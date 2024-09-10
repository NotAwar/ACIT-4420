# Base class 
class BankAccount:
    def _init_(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        
    def deposit(self, ammount):
        self.balance += ammount

    def withdraw(self, ammount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def account_info(self):
        return f"Account holder: {self.account_holder}, Balance: ${self.balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, interest_rate=0.02):
        super().__init__(account_holder)  # Initialize BankAccount attributes
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest of ${interest:.2f}. New balance is ${self.balance:.2f}")