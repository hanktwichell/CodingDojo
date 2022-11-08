int_rates_key = [{
    'Investment': 0.04,
    'Checking': 0.01,
    'Savings': 0.025
}]


class User:
    all_users = []
    all_accounts = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account_list = []
        User.all_users.append(self)

    def create_account(self, account_type, account_name, amount):
        for acca in User.all_accounts:
            if (acca.account_name == account_name):
                print(
                    f"An Account With The Name \"{account_name}\" Already Exists")
                return self
        new_account = Account(account_type, account_name, int_rate=int_rates_key[0][account_type], balance=amount)
        User.all_accounts.append(new_account)
        self.account_list.append(new_account)
        return self

    def make_deposit(self, amount, account_name):
        index = 0
        for acca in self.account_list:
            if (acca.account_name == account_name):
                self.account_list[index].deposit(amount)
                return self
            else:
                index += 1
        print(f"No Account With Name \"{account_name}\" Exists")
        User.create_account(self, "Savings", account_name, amount)
        return self

    def make_withdrawl(self, amount, account_name):
        index = 0
        for acca in self.account_list:
            if (acca.account_name == account_name):
                self.account_list[index].withdraw(amount)
                return self
            else:
                index += 1
        print(f"No Account With Name \"{account_name}\" Exists")
        return self

    def interest_yield(self, account_name):
        index = 0
        for acca in self.account_list:
            if (acca.account_name == account_name):
                self.account_list[index].yield_interest()
                return self
            else:
                index += 1
        return self

    def display_user_balance(self, account_name):
        index = 0
        for acca in self.account_list:
            if (acca.account_name == account_name):
                print(
                    f"{account_name} Balance: ${self.account_list[index].balance:,.2f}")
                return self
            else:
                index += 1
        return self

    def display_info(self, account_name):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        index = 0
        for acca in self.account_list:
            if (acca.account_name == account_name):
                print(f"Account Name: {self.account_list[index].account_name}")
                print(f"Account Type: {self.account_list[index].account_type}")
                print(
                    f"Account Balance: ${self.account_list[index].balance:,.2f}")
                print(
                    f"Account Interest Rate: {self.account_list[index].int_rate*100:.2f}%")
                return self
            else:
                index += 1
        return self

    def transfer_money(self, source_account, amount, other_account):
        index = 0
        index2 = 0
        for acca in self.account_list:
            if (acca.account_name == source_account):
                self.account_list[index].withdraw(amount)
            else:
                index += 1
        for acca2 in User.all_accounts:
            if (acca2.account_name == other_account):
                acca2.deposit(amount)
            else:
                index2 += 1
        return self

    @classmethod
    def list_all_accounts(cls):
        for user_acca in cls.all_user_accounts:
            print("================================")
            print(f"Account Name: {user_acca.account_name}")
            print(f"Account Type: {user_acca.account_type}")
            print(f"Account Balance: ${user_acca.balance:,.2f}")
            print(f"Account Interest Rate: {user_acca.int_rate*100:.2f}%")
            print("================================")

    @classmethod
    def list_all_users(cls):
        for user in cls.all_users:
            print(user.first_name, user.last_name)

    def list_all_user_accounts(self):
        print("================================")
        print(f"{self.first_name} {self.last_name}'s Accounts:")
        for acca in self.account_list:
            print("-----------")
            print(f"Account Name: {acca.account_name}")
            print(f"Account Type: {acca.account_type}")
            print(f"Account Balance: ${acca.balance:,.2f}")
            print(f"Account Interest Rate: {acca.int_rate*100:.2f}%")
        print("================================")


class Account:
    account_balance = 0.00
    all_accounts = []

    def __init__(self, account_type, account_name, int_rate, balance):
        self.account_type = account_type
        self.account_name = account_name
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
                f"Account Owner: ???, Account Name: {account.account_name}, Account Type: {account.account_type}, Account Balance: {account.balance:,.2f}, Interest Rate {account.int_rate*100:.2f}%")


adrian = User("Adrian", "Newey")
adrian.create_account("Savings", "Newey Savings", 20000).make_deposit(5000, "Newey Savings").create_account("Checking", "Newey Checking", 2000).make_deposit(7000, "Newey Checking").make_withdrawl(2000, "Newey Checking").create_account("Investment", "Newey Investment", 5000).create_account("Checking", "Newey Savings", 2000).transfer_money("Newey Savings", 15000, "Megan Savings")
megan = User("Megan", "Johnson")
megan.create_account("Savings", "Johnson Savings", 3000).make_deposit(4000, "Johnson Savings").create_account("Savings", "Megan Savings", 69000).make_withdrawl(70000, "Megan Savings").interest_yield("Megan Savings").transfer_money("Megan Savings", 70000, "Newey Investment")
User.list_all_users()
adrian.list_all_user_accounts()
megan.list_all_user_accounts()
