class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")


my_dog = Dog("Willine", 3)
your_dog = Dog("Frag", 4)
my_dog.roll_over()
my_dog.sit()
print(f"My dog's name is {my_dog.name}, {my_dog.age} years old")
print(f"Your dog's name is {your_dog.name}, {your_dog.age} years old")

##########################################################################
