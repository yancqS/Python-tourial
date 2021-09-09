# 使用and检查多个条件
age_0 = 22
age_1 = 18

print(age_0 >= 21 and age_1 >= 21)  # False

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)  # True

# 使用or检查多个条件
age_0 = 22
age_1 = 18

print(age_0 >= 21 or age_1 >= 21)  # True

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)  # False

list_1 = ['mushroom', 'onions', 'pineapple']
print('mushroom' in list_1)  # True
print('pepperoni' in list_1)  # False

ban_users = ['andrew', 'carlion', 'david']
user = 'marie'

if user not in ban_users:
    print(f'{user.title()}, you can post a response if you wash')

# if语句

age = 19
if age > 18:
    print('You are old enough to vote')

# if-else语句

age = 19
if age > 18:
    print('You are old enough to vote')
else:
    print('Sorry, you are too young to vote')

# if-elif-else语句
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f'Your admission cost is ${price}')
# Your admission cost is $25

# 使用多个elif代码块

age = 68
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f'Your admission cost is ${price}')

# 省略else代码块

age = 68
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f'Your admission cost is ${price}')

# 测试多个条件

request_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in request_topping:
    print('Adding mushrooms')
if 'pepperoni' in request_topping:
    print('Adding pepperoni')
if 'extra cheese' in request_topping:
    print('Adding extra cheese')

print('Finished !')


request_topping = ['mushrooms',  'green peppers', 'extra cheese']

for value in request_topping:
    if value == 'green peppers':
        print('Sorry, we are out of green peppers right now')
    else:
        print(f'Adding {value}')

print('Finished !')


request_topping = []

if request_topping:
    for value in request_topping:
        print(f'Adding {value}')
    print('Finished !')
else:
    print('Are you sure you want a plain pizza')


avaliable_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

request_toppings = ['mushrooms', 'french fries', 'extra cheese']

for request_topping in request_toppings:
    if request_topping in avaliable_toppings:
        print(f'Adding {request_topping}')
    else:
        print(f"Sorry, we don't have {request_topping}")

print('Finished !')
