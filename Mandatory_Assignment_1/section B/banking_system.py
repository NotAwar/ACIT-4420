import typer
import json
import os

# File to store account data
DB_FILE = "accounts_db.json"

# Load accounts from the file if it exists
def load_accounts():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}

# Save accounts to the file
def save_accounts(accounts_db):
    with open(DB_FILE, "w") as f:
        json.dump(accounts_db, f, indent=4)

# Initialize accounts_db from the file
accounts_db = load_accounts()

# Base class: BankAccount
class BankAccount:
    def __init__(self, account_holder: str):
        self.account_holder = account_holder
        self.balance = 0.0  # Initialize balance to 0
    
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}")
        else:
            print("Insufficient funds.")
    
    def account_info(self):
        return f"Account holder: {self.account_holder}, Balance: ${self.balance:.2f}"

# Derived class: SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder: str, interest_rate: float = 0.02):
        super().__init__(account_holder)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest of ${interest:.2f}. New balance is ${self.balance:.2f}")

# Derived class: CheckingAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_holder: str, transaction_fee: float = 1.0):
        super().__init__(account_holder)
        self.transaction_fee = transaction_fee
    
    def withdraw(self, amount: float):
        total_withdrawal = amount + self.transaction_fee
        if total_withdrawal <= self.balance:
            self.balance -= total_withdrawal
            print(f"Withdrew ${amount:.2f} with a ${self.transaction_fee:.2f} fee. New balance is ${self.balance:.2f}")
        else:
            print("Insufficient funds for this transaction including the fee.")

# Helper function to get account by name from accounts_db
def get_account(name: str):
    if name in accounts_db:
        account_data = accounts_db[name]
        if account_data["type"] == "savings":
            account = SavingsAccount(account_data["account_holder"], account_data["interest_rate"])
        elif account_data["type"] == "checking":
            account = CheckingAccount(account_data["account_holder"], account_data["transaction_fee"])
        else:
            account = BankAccount(account_data["account_holder"])
        
        account.balance = account_data["balance"]
        return account
    else:
        print(f"Account for {name} does not exist.")
        raise typer.Exit()

# Update account information in accounts_db
def update_account_in_db(account):
    accounts_db[account.account_holder] = {
        "account_holder": account.account_holder,
        "balance": account.balance,
        "type": "savings" if isinstance(account, SavingsAccount) else "checking" if isinstance(account, CheckingAccount) else "standard",
        "interest_rate": account.interest_rate if isinstance(account, SavingsAccount) else None,
        "transaction_fee": account.transaction_fee if isinstance(account, CheckingAccount) else None
    }
    save_accounts(accounts_db)

# Typer app for command-line interaction
app = typer.Typer()

@app.command()
def create_account(account_type: str, name: str, interest_rate: float = 0.02, transaction_fee: float = 1.0):
    """Create a new account based on type: savings or checking."""
    if account_type.lower() == 'savings':
        account = SavingsAccount(name, interest_rate)
    elif account_type.lower() == 'checking':
        account = CheckingAccount(name, transaction_fee)
    else:
        account = BankAccount(name)
    
    update_account_in_db(account)
    typer.echo(account.account_info())

@app.command()
def deposit(name: str, amount: float):
    """Deposit an amount into the account."""
    account = get_account(name)
    account.deposit(amount)
    update_account_in_db(account)

@app.command()
def withdraw(name: str, amount: float):
    """Withdraw an amount from the account."""
    account = get_account(name)
    account.withdraw(amount)
    update_account_in_db(account)

@app.command()
def apply_interest(name: str):
    """Apply interest to a savings account."""
    account = get_account(name)
    if isinstance(account, SavingsAccount):
        account.apply_interest()
        update_account_in_db(account)
    else:
        print(f"{name} does not have a savings account.")

@app.command()
def account_info(name: str):
    """Display the account information."""
    account = get_account(name)
    typer.echo(account.account_info())

if __name__ == "__main__":
    app()






# "python .\banking_system.py --help" will display the help menu with all arguments and commands
# │ account-info                      Display the account information.                                                                                             │
# │ apply-interest                    Apply interest to a savings account.                                                                                         │
# │ create-account                    Create a new account based on type: savings or checking.                                                                     │
# │ deposit                           Deposit an amount into the account.                                                                                          │
# │ withdraw                          Withdraw an amount from the account.   