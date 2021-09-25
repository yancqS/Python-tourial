from commonCar import Car, EcarSec as eCar

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

my_e_car = eCar('tesla', 'model S', 2019, 100)
long_name_e = my_e_car.get_descriptive_name()
print(long_name_e)
my_e_car.battery.get_bettery()

# 导入整个模块

import commonCar

my_new_car = commonCar.Car('audi', 'a4', 2019)
long_name = my_new_car.get_descriptive_name()
print(long_name)

my_e_car = commonCar.EcarSec('tesla', 'model S', 2019, 799)
long_name_e = my_e_car.get_descriptive_name()
print(long_name_e)
my_e_car.battery.get_bettery()
