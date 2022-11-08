print()

# NO CREATE ACCOUNT METHOD

class User:
    all_user_accounts = []

    def __init__(self, first_name, last_name, account_type, account_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account_type = account_type
        self.account_name = account_name
        if (account_type == "Savings"):
            self.account = Account(int_rate=0.025, balance=0.00)
        else:
            self.account = Account(int_rate=0.01, balance=0.00)
        User.all_user_accounts.append(self)

    def make_deposit(self, amount, account_type):
        self.account.deposit(amount, account_type)
        return self

    def make_withdrawl(self, amount, account_type):
        self.account.withdraw(amount, account_type)
        return self

    def display_user_balance(self, account_type):
        print(f"{account_type} Balance: ${self.account.balance:,.2f}")
        return self

    def display_info(self, account_type):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Account Type: {self.account_type}")
        print(f"Account Balance: ${self.account.balance:,.2f}")
        print(f"Interest Rate: {self.int_rate*100:.2f}%")
        return self

    @classmethod
    def list__all_accounts(cls):
        for user_account in cls.all_user_accounts:
            print("FN", user_account.first_name)
            print("LN", user_account.last_name)
            print("AN", user_account.account_name)
            print("AT", user_account.account_type)

class Account:
    account_balance = 0.00
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        Account.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (amount > self.balance):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance:,.2f}")
        return self

    def yield_interest(self):
        if (self.balance >= 0):
            self.balance *= (1+self.int_rate)
        return self

    @classmethod
    def all_instances(cls):
        for account in cls.all_accounts:
            print(f"Account Balance: {account.balance}, Interest Rate {account.int_rate}")


adrian_checking = User("Adrian", "Newey", "Checking", "Newey Checking")
adrian_savings = User("Adrian", "Newey", "Savings", "Newey Savings")
# adrian.create_account("Savings", "Newey Savings")
User.list__all_accounts()
# adrian.make_deposit(5000, "Checking").make_withdrawl(2000, "Savings").display_user_balance("Savings").display_info("Checking")
