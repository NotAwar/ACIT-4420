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
    