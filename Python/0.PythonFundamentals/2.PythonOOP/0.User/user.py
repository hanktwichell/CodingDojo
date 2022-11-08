class User:
    def __init__ (self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")

    def enroll(self):
        if (self.is_rewards_member):
            print(f"{self.first_name} {self.last_name} is already a rewards member.")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200
        print(f"{self.first_name} {self.last_name} is now a rewards member! {self.first_name} has {self.gold_card_points} Gold Card points")
        return True

    def spend_points(self, amount):
        if (not self.is_rewards_member):
            print(f"{self.first_name} {self.last_name} is not a rewards member and has no points.")
        elif (amount > self.gold_card_points):
            print(
                f"Insufficient Point Balance. {self.first_name} {self.last_name} Remaining Point Balance: {self.gold_card_points}")
        else:
            self.gold_card_points -= amount
            print(f"{self.first_name} {self.last_name} Remaining Point Balance: {self.gold_card_points}")

user_john = User("John", "Doe", "johndoe@gmail.com", 36)
user_john.display_info()
user_john.enroll()
user_molly = User("Molly", "Taylor", "mollytaylor@RXR.com", 24)
user_sergio = User("Sergio", "Perez", "checo@redbull.com", 32)
user_john.spend_points(50)
user_molly.enroll()
user_molly.spend_points(80)
user_john.display_info()
user_molly.display_info()
user_sergio.display_info()
user_john.enroll()
user_sergio.spend_points(40)
user_sergio.enroll()
user_sergio.spend_points(400)