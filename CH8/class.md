## 第九章 类

### 创建和使用类

```python
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
```

类中的函数称为**方法**。`__init__`是一个特殊的方法，每当你根据`Dog`类创建新实例时，Python都会自动运行它。以`self`为前缀的变量可供类中的所有方法使用，可以供类的任何实例来访问。像这种可以通过实例来访问的变量称为**属性**。

> `__init__`方法类似与JS类中`constructor`方法，`self`相当于`this`.

### 使用类和实例

我们首先写一个表示汽车的类：

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
```

在创建实例时，有些属性无需通过形参来定义，可在`__init__`方法中为其指定默认值。下面我们创建一个属性，并且其初始值为0；再创建一个方法来读取这个属性的值。

```diff
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
+       self.meter = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
+   def get_meter(self):
+       print(f"This car has {self.meter} miles on it")
```

#### 修改属性值

- 直接修改属性的值

要修改属性的值最简单的方式是通过**实例**直接访问它。

```python
my_new_car = Car('audi', 'a4', 2019)
my_new_car.get_meter()
my_new_car.meter = 50
my_new_car.get_meter()
```

- 通过方法修改属性的值

```python
class Car:
  --snip--
  def update_meter(self, meter):
      if meter > self.meter:
          self.meter = meter
      else:
          print("You can't roll back an meter")
          

my_new_car = Car('audi', 'a4', 2019)
long_name = my_new_car.get_descriptive_name()
print(long_name)
my_new_car.get_meter()
my_new_car.meter = 50
my_new_car.get_meter()

print('*' * 40)

my_new_car.update_meter(80)
my_new_car.update_meter(30)
my_new_car.get_meter()
```

输出为：

```
2019 audi a4
This car has 0 miles on it
This car has 50 miles on it
****************************************
You can't roll back an meter
This car has 80 miles on it
```

- 通过方法对属性的值进行递增

```diff
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

+   def increment_meter(self, miles):
+       self.meter += miles
```

### 继承

编写类时，并非总要从空白开始，如果要编写的类是另一个现成类的特殊版本，可以使用**继承**。一个类**继承**另一个类时，将自动获得另一个类的所有属性和方法。原有的类称为**父类**，而新类称为**子类**。

在既有类的基础上编写新类时，通常要调用父类的方法`__init__()`。这将初始化在父类`__init__()`方法中定义的所有属性，从而让子类包含这些属性。

```python
class E_car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


my_e_car = E_car('tesla', 'model S', 2019)
long_name_e = my_e_car.get_descriptive_name()
print(long_name_e) # 2019 tesla model S
```

#### 给子类定义属性和方法

```python
class E_car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = 75

    def get_bettery(self):
        print(f"This car has a {self.battery}-kwh battery")


my_e_car = E_car('tesla', 'model S', 2019)
long_name_e = my_e_car.get_descriptive_name()
print(long_name_e)
my_e_car.get_bettery()
```

输出为：

```
2019 tesla model S
This car has a 75-kwh battery
```

#### 重写父类的方法

可在子类中定义一个与要重写的父类方法同名的方法。这样Python将不会考虑这个父类方法，而只关注在子类中定义的相关方法。

```python
class E_car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = 75

    def get_bettery(self):
        print(f"This car has a {self.battery}-kwh battery")

    def get_descriptive_name(self):
        long_name = f"e_car info: {self.year} {self.make} {self.model}"
        return long_name


my_e_car = E_car('tesla', 'model S', 2019)
long_name_e = my_e_car.get_descriptive_name()
print(long_name_e)
my_e_car.get_bettery()
```

输出为：

```
e_car info: 2019 tesla model S
This car has a 75-kwh battery
```

#### 将实例用作属性

当给类添加的细节越多时，属性和方法清单及文件都越来越长。在这种情况下，可能需要将类的一部分提取出来，作为一个独立的类。可以将大型类拆分为多个协同工作的小型类。

```python
class E_car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def get_descriptive_name(self):
        long_name = f"e_car info: {self.year} {self.make} {self.model}"
        return long_name


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def get_bettery(self):
        print(f"This car has a {self.battery_size}-kwh battery")


my_e_car = E_car('tesla', 'model S', 2019)
long_name_e = my_e_car.get_descriptive_name()
print(long_name_e)
my_e_car.battery.get_bettery()
```

输出为：

```
e_car info: 2019 tesla model S
This car has a 75-kwh battery
```

### 导入类

随着不断给类添加功能，文件可能会变的很长，即便稳妥的使用了继承亦是如此。为遵循Python的总体理念，应该让文件尽可能整洁。Python在这方面提供了帮助，允许将类储存在模块中，然后在主程序中导入所需的模块。

#### 导入单个类

将Car类单独放在一个文件`car.py`模块中

```python
cars.py
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
```

然后在另外一个文件`my_car.py`中，在其中导入`Car`类并创建其实例：

```python
myCar.py
from car import Car

my_new_car = Car('audi', 'a4', 2019)
long_name = my_new_car.get_descriptive_name()
print(long_name)
my_new_car.get_meter()
my_new_car.meter = 50
my_new_car.get_meter()
```

输出为：

```
2019 audi a4
This car has 0 miles on it
This car has 50 miles on it
```

#### 在一个模块中存储多个类、从一个模块中导入多个类

把`E_car`类和`Battery`类都放到`car.py`中,然后在`my_car.py`中把这些类导入：

```python
myCar.py
from car import Car, E_car

my_new_car = Car('audi', 'a4', 2019)
long_name = my_new_car.get_descriptive_name()
print(long_name)
my_new_car.get_meter()
my_new_car.meter = 50
my_new_car.get_meter()

print('*' * 40)

my_new_car.update_meter(80)
my_new_car.update_meter(30)
my_new_car.get_meter()
my_new_car.increment_meter(20)
my_new_car.get_meter()

print('+' * 40)

my_e_car = E_car('tesla', 'model S', 2019)
long_name_e = my_e_car.get_descriptive_name()
print(long_name_e)
my_e_car.battery.get_bettery()
```

输出为：

```
2019 audi a4
This car has 0 miles on it
This car has 50 miles on it
****************************************
You can't roll back an meter
This car has 80 miles on it
This car has 100 miles on it
++++++++++++++++++++++++++++++++++++++++
e_car info: 2019 tesla model S
This car has a 100-kwh battery
```

#### 导入整个模块

```python
import car

my_new_car = car.Car('audi', 'a4', 2019)

my_e_car = car.E_car('tesla', 'model S', 2019)
```

#### 导入模块中所有的类

语法：from *module_name* import *

> 不推荐这种写法。

#### 在一个模块中导入另一个模块

把`Battery`类单独放到`battery.py`文件，然后在`car.py`中引入（因为E_car类的battery属性是Battery类的实例）：

```python
# car.py
from battery import Battery

class Car:
  # ....

class E_car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(100)

    def get_descriptive_name(self):
        long_name = f"e_car info: {self.year} {self.make} {self.model}"
        return long_name
```

#### 使用别名

```python
from car import E_car as EC, Car
```