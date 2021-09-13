## 字典

在python中，**字典**是一系列**键值对**。每个键都与一个值相关联,可以使用键来访问相关联的值。与键相关联的值可以是数、字符串、列表乃至字典。

### 使用字典

```Python
# 获取字典中的值
alien_0 = {
    'color': 'yellow'
}
print(alien_0['color']) # yellow

# 添加键值对

alien_1 = {}

alien_1['x_pos'] = 20
alien_1['y_pos'] = 30

print(alien_1) # {'x_pos': 20, 'y_pos': 30}

# 修改字典中的值

alien_1['x_pos'] = 50

print(alien_1) # {'x_pos': 50, 'y_pos': 30}

# 删除键值对
# 使用del语句时，必须要指定字典明和要删除的键
del alien_1['x_pos']

print(alien_1) # {'y_pos': 30}
```

### 使用get()方法来访问值

使用放在方括号内的键从字典中获取相关联的值时，如果指定的键不存在就会出错。

```Python
favorite_language = {
    'Tom': 'c'
}

print(favorite_language['John'])

# 报错
# Traceback (most recent call last):
#   File "simple_message.py", line 188, in <module>
#     print(favorite_language['John'])
# KeyError: 'John'

```

可以使用get()方法在指定的键不存在时返回一个默认值，从而避免这样的错误。

get()方法的第一个参数用于指定键，是必不可少的，第二个参数为指定的键不存在时要返回的值，是可选的。

```Python
favorite_language = {
    'Tom': 'c'
}

language = favorite_language.get('Tom', 'Python')
print(f'favorite language: {language}') #  favorite language: c

language = favorite_language.get('John', 'Python')
print(f'favorite language: {language}') #  favorite language: Python
```

>调用get()方法时，如果没有指定第二个参数且指定的键不存在时，Python将返回`None`。

### 遍历字典

```Python
favorite_language = {
    'Tom': 'c',
    'Eric': 'Java'
}

print(favorite_language.items())
print(favorite_language.keys())
print(favorite_language.values())
```

输出为：

```
dict_items([('Tom', 'c'), ('Eric', 'Java')])
dict_keys(['Tom', 'Eric'])
dict_values(['c', 'Java'])
```

因此我们可以遍历字典的所有键值对、所有键、所有值。

首先是遍历**键值对**：

```Python
favorite_language = {
    'Tom': 'c',
    'Eric': 'Java'
}

for k, v in favorite_language.items():
    print(f'Key: {k}', end='\t')
    print(f'Value: {v}')
```

然后时遍历字典中的**键**：

```Python
favorite_language = {
    'Tom': 'c',
    'Eric': 'Java'
}

for k in favorite_language.keys():
    print(f'Key: {k}')
```

遍历字典时，会默认遍历所有的键。因此上述代码中的：

```Python
for k in favorite_language.keys():
```

替换为：

```Python
for k in favorite_language:
```

输出将不变。

按照特定顺序遍历字典中的所有键：

>从 python3.7 起，遍历字典时将按照插入的顺序返回其中的元素。

要以特定顺序返回元素，可以使用`sorted()`来获得按特定顺序排列的键列表的副本：

```Python
favorite_language = {
    'Tom': 'c',
    'Eric': 'Java',
    'Alice': 'ruby'
}

for name in sorted(favorite_language.keys()):
    print(name, favorite_language[name])

print('*' * 40)

for name in sorted(favorite_language.keys(), reverse=True):
    print(name, favorite_language[name])
```

输出为：

```Python
Alice ruby
Eric Java
Tom c
****************************************
Tom c
Eric Java
Alice ruby
```

然后时遍历字典中所有**值**：

```Python
favorite_language = {
    'Tom': 'c',
    'Eric': 'Java',
    'Alice': 'ruby',
    'phil': 'ruby'
}

for v in favorite_language.values():
    print(f'Value: {v}')
```

输出为：

```
Value: c
Value: Java
Value: ruby
Value: ruby
```

这种做法时提取字典中所有的值，没有考虑重复项。为了剔除重复项，可以使用**集合(set)**。集合中的每个元素都必须时独一无二的。

```Python
favorite_language = {
    'Tom': 'c',
    'Eric': 'Java',
    'Alice': 'ruby',
    'phil': 'ruby'
}

for v in set(favorite_language.values()):
    print(f'Value: {v}')
```

输出为：

```
Value: Java
Value: ruby
Value: c
```

**注意：**

可以使用一对花括号直接创建**集合**，并在其中用逗号分隔元素：

```Python
languages = {'c', 'java', 'ruby', 'java'}
print(languages) #  {'c', 'ruby', 'java'}
```

集合和字典很容易混淆，因为它们都是用一对花括号定义的。当花括号内没有键值对时。定义的很可能是集合。**不同于列表和字典，集合不会以特定的顺序存储元素。**

### 嵌套

#### 字典列表

```Python
alien_0 = {'color': 'green', 'point': 5}
alien_1 = {'color': 'green', 'point': 6}
alien_2 = {'color': 'green', 'point': 7}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    if alien['point'] == 5:
        alien['color'] = 'red'
        alien['point'] = 10

print(aliens)
```

### 字典中存储列表

```Python
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

for topping in pizza['toppings']:
    print('\t' + topping)
```

### 字典中存储字典

```Python
users = {
    'Tom': {
        'first': 'tom',
        'second': 'twice',
        'location': 'beijing'
    },
    'john': {
        'first': 'john',
        'second': 'eric',
        'location': 'shandong'
    }
}

for username, user_info in users.items():
    print(f'\nUsername: {username}')
    full_name = f'{user_info["first"]} {user_info["second"]}'
    location = user_info['location']

    print(f'\tFull name: {full_name.title()}')
    print(f'\tLocation: {location.title()}')
```