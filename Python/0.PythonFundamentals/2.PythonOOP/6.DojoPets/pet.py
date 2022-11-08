import ninja

class Pet:
    def __init__(self, name, type, tricks):
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

class Dog(Pet):
    def __init__ (self, name, type, tricks):
        super().__init__(name, type, tricks)
        self.energy = 90
        self.health = 75
        self.hunger = 60
        self.sound = "Woof"
    def noise(self):
        print(f"{self.name} says \"{self.sound}!\"")

class Cat(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
        self.energy = 50
        self.health = 85
        self.hunger = 30
        self.sound = "Meow"
        print(f"{self.name} says \"{self.sound}!\"")


pet_spike = Dog("Spike", "Dog", {"Sit", "Shake", "Stay", "Play Dead"})
ninja_john = ninja.Ninja("John", "Doe", {"Chicken", "Bacon"}, "Salmon", pet_spike).walk().feed().bathe()
