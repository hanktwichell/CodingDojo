class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    def walk(self):
        print(f"Taking {self.pet.name} for a walk!")
        self.pet.play()
        return self
    def feed(self):
        print(f"Feeding {self.pet.name}!")
        self.pet.eat()
        return self
    def bathe(self):
        print(f"Bathing {self.pet.name}!")
        self.pet.noise()
        return self

class Pet:
    def __init__ (self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 80
        self.energy = 80
        self.hunger = 50
    def sleep(self):
        if (self.energy + 25 >= 100):
            self.energy = 100
        else:
            self.energy += 25
        if (self.health + 5 >= 100):
            self.health = 100
        else:
            self.health += 5
        return self
    def eat(self):
        if (self.hunger == 0):
            print(f"{self.name} cannot eat another bite!")
        elif (self.hunger - 25 <= 0):
            self.hunger = 0
            print(f"Yum! {self.name} is all full!")
        else:
            self.hunger -= 25
            print("Yummy!")
        if (self.health + 10 >= 100):
            self.health = 100
        else:
            self.health += 10
        if (self.energy + 5 >= 100):
            self.energy = 100
        else:
            self.energy += 5
        return self
    def play(self):
        print("Playing!")
        if (self.energy - 15 < 0):
            print(f"{self.name} is too tired to play!")
        elif (self.hunger + 20 > 100):
            print(f"{self.name} is too hungry to play!")
        else:
            if (self.health + 5 >= 100):
                self.health = 100
            else:
                self.health += 5
            if (self.energy - 10 <= 0):
                self.energy = 0
            else:
                self.energy -= 10
            if (self.hunger + 20 >= 100):
                self.hunger = 100
            else:
                self.hunger += 20
        return self
    def noise(self):
        if self.type == "Dog":
            print(f"{self.name} says \"Woof!\"")
        elif self.type == "Cat":
            print(f"{self.name} says \"Meow!\"")
        else:
            print(f"{self.name} says \"...!\"")

pet_spike = Pet("Spike", "Dog", {"Sit", "Shake", "Stay", "Play Dead"})
ninja_john = Ninja("John", "Doe", {"Chicken", "Bacon"}, "Salmon", pet_spike).walk().feed().bathe()