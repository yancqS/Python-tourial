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

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.meter = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def get_meter(self):
        print(f"This car has {self.meter} miles on it")

    def update_meter(self, meter):
        if meter > self.meter:
            self.meter = meter
        else:
            print("You can't roll back an meter")

    def increment_meter(self, miles):
        self.meter += miles

# 修改属性值-直接修改属性值


my_new_car = Car('audi', 'a4', 2019)
my_new_car.get_meter()
my_new_car.meter = 50
my_new_car.get_meter()

# 通过方法修改属性值

print('*' * 40)

my_new_car.update_meter(80)
my_new_car.update_meter(30)
my_new_car.get_meter()

# 通过方法对属性的值进行递增

my_new_car.increment_meter(20)
my_new_car.get_meter()

##########################################################################

# 继承


class Ecar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = 75

    def get_bettery(self):
        print(f"This car has a {self.battery}-kwh battery")

    # 重新父类的方法
    def get_descriptive_name(self):
        long_name = f"e_car info: {self.year} {self.make} {self.model}"
        return long_name


my_e_car = Ecar('tesla', 'model S', 2019)
long_name_e = my_e_car.get_descriptive_name()
print(long_name_e)  # 2019 tesla model S
my_e_car.get_bettery()

##########################################################################

# 将实例用作属性


class EcarSec(Car):
    def __init__(self, make, model, year, battery):
        super().__init__(make, model, year)
        self.battery = Battery(battery)

    def get_descriptive_name(self):
        long_name = f"e_car info: {self.year} {self.make} {self.model}"
        return long_name


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def get_bettery(self):
        print(f"This car has a {self.battery_size}-kwh battery")


my_e_car = EcarSec('tesla', 'model S', 2019, 100)
long_name_e = my_e_car.get_descriptive_name()
print(long_name_e)
my_e_car.battery.get_bettery()

##########################################################################

# 导入类




