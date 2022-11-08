class User:
    def __init__(self, first_name, last_name, email, age):
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
        return self

    def enroll(self):
        if (self.is_rewards_member):
            print(f"{self.first_name} {self.last_name} is already a rewards member.")
        self.is_rewards_member = True
        self.gold_card_points = 200
        print(f"{self.first_name} {self.last_name} is now a rewards member! {self.first_name} has {self.gold_card_points} Gold Card points")
        return self

    def spend_points(self, amount):
        if (not self.is_rewards_member):
            print(
                f"{self.first_name} {self.last_name} is not a rewards member and has no points.")
        elif (amount > self.gold_card_points):
            print(
                f"Insufficient Point Balance. {self.first_name} {self.last_name} Remaining Point Balance: {self.gold_card_points}")
        else:
            self.gold_card_points -= amount
            print(
                f"{self.first_name} {self.last_name} spent {amount} points! Remaining Point Balance: {self.gold_card_points}")
        return self


user_john = User("John", "Doe", "johndoe@gmail.com", 36)
user_john.display_info().enroll().spend_points(50).enroll()
user_molly = User("Molly", "Taylor", "mollytaylor@RXR.com", 24)
user_sergio = User("Sergio", "Perez", "checo@redbull.com", 32)
user_molly.enroll().spend_points(80).display_info()
user_sergio.display_info().spend_points(40).enroll().spend_points(400)
