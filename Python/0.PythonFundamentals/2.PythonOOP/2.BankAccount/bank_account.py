class Account:
    account_balance = 0
    all_accounts = []

    def __init__(self, account_type, int_rate, balance):
        self.account_type = account_type
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
        self.balance = "{:.2f}".format(self.balance)
        print(f"{self.account_type} Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if (self.balance >= 0):
            self.balance *= (1+self.int_rate)
        return self

    @classmethod
    def all_instances(cls):
        for account in cls.all_accounts:
            print(f"Account Type: {account.account_type}, Account Balance: {account.balance}, Interest Rate {account.int_rate}")

john_checking = Account("Checking", 0.01, 0)
amy_savings = Account("Savings", 0.04, 1000)
john_checking.deposit(1000).deposit(5000).deposit(10000).withdraw(4000).yield_interest().display_account_info()
amy_savings.deposit(20000).deposit(750).withdraw(250).withdraw(450).withdraw(5000).withdraw(69.69).display_account_info()
Account.all_instances()