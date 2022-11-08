
print()


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account = Account(int_rate=0.02, balance=0.00)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"Balance: ${self.account.balance:,.2f}")
        return self

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Account Balance: ${self.account.balance:,.2f}")
        print(f"Interest Rate: {self.account.int_rate*100:.2f}%")
        return self


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
            print(
                f"Account Balance: {account.balance}, Interest Rate {account.int_rate}")


adrian = User("Adrian", "Newey")
adrian.make_deposit(5000).make_withdrawl(2000).display_info()
