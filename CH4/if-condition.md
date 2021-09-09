## if语句

### 检查多个条件

```Python
# 使用and检查多个条件
age_0 = 22
age_1 = 18

age_0 >= 21 and age_1 >= 21 #  False

age_1 = 22
age_0 >= 21 and age_1 >= 21 #  True

# 使用or检查多个条件
age_0 = 22
age_1 = 18

age_0 >= 21 or age_1 >= 21 #  True

age_0 = 18
age_0 >= 21 or age_1 >= 21 #  False
```

检查特定值是否包含在列表中:

```Python
list_1 = ['mushroom', 'onions', 'pineapple']
'mushroom' in list_1 # True
'pepperoni' in list_1 # False 
```

检查特定值是否不包含在列表中:

```Python
ban_users = ['andrew', 'carlion', 'david']
user = 'marie'

if user not in ban_users:
    print(f'{user.title()}, you can post a response if you wash')
```

### if语句/if-else语句/if-elif-else语句

```Python
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
```

### 使用多个elif代码块

```Python
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
```

### 省略else代码块

python并不要求if-elif结构后面必须游else代码块。

```Python
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
```

### 测试多个条件

`if-elif-else`结构功能强大，但是仅适合用于只有一个条件满足的情况：遇到通过了的测试后，python就跳过余下的测试。

然而，有时候必须检查你关心的所有条件，在这种情况下，应使用一系列不包含elif和else代码块的简单if语句。在存在多个条件为True且需要在每个条件为True时都采取相应措施时，适合用这种方法。

```Python
request_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in request_topping:
    print('Adding mushrooms')
if 'pepperoni' in request_topping:
    print('Adding pepperoni')
if 'extra cheese' in request_topping:
    print('Adding extra cheese')
    
print('Finished !')
```

### if语句处理列表

#### 检查特殊元素

```Python
request_topping = ['mushrooms',  'green peppers', 'extra cheese']

for value in request_topping:
    if value == 'green peppers':
        print('Sorry, we are out of green peppers right now')
    else:
        print(f'Adding {value}')

print('Finished !')
```

#### 确定列表不是空的

```Python
request_topping = []

if request_topping:
    for value in request_topping:
        print(f'Adding {value}')
    print('Finished !')
else:
    print('Are you sure you want a plain pizza')
```

### 使用多个列表

```Python
avaliable_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

request_toppings = ['mushrooms', 'french fries', 'extra cheese']

for request_topping in request_toppings:
    if request_topping in avaliable_toppings:
        print(f'Adding {request_topping}')
    else:
        print(f"Sorry, we don't have {request_topping}")

print('Finished !')
```

输出为：

```
Adding mushrooms
Sorry, we don't have french fries
Adding extra cheese
Finished !
```