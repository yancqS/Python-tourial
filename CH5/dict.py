# 获取字典中的值
alien_0 = {
    'color': 'yellow'
}
print(alien_0['color'])  # yellow

# 添加键值对

alien_1 = {}

alien_1['x_pos'] = 20
alien_1['y_pos'] = 30

print(alien_1)  # {'x_pos': 20, 'y_pos': 30}

# 修改字典中的值

alien_1['x_pos'] = 50

print(alien_1) # {'x_pos': 50, 'y_pos': 30}

# 删除键值对
# 使用del语句时，必须要指定字典明和要删除的键
del alien_1['x_pos']

print(alien_1)  # {'y_pos': 30}

# favorite_language = {
#     'Tom': 'c'
# }
#
# print(favorite_language['John'])

# 报错
# Traceback (most recent call last):
#   File "dict.py", line 32, in <module>
#     print(favorite_language['John'])
# KeyError: 'John'


favorite_language = {
    'Tom': 'c'
}

language = favorite_language.get('Tom', 'Python')
print(f'favorite language: {language}')  # favorite language: c

language = favorite_language.get('John', 'Python')
print(f'favorite language: {language}')  # favorite language: Python

favorite_language = {
    'Tom': 'c',
    'Eric': 'Java'
}

print(favorite_language.items())
print(favorite_language.keys())
print(favorite_language.values())

favorite_language = {
    'Tom': 'c',
    'Eric': 'Java'
}

for k, v in favorite_language.items():
    print(f'Key: {k}', end='\t')
    print(f'Value: {v}')


favorite_language = {
    'Tom': 'c',
    'Eric': 'Java'
}

for k in favorite_language.keys():
    print(f'Key: {k}')


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


favorite_language = {
    'Tom': 'c',
    'Eric': 'Java',
    'Alice': 'ruby',
    'phil': 'ruby'
}

for v in favorite_language.values():
    print(f'Value: {v}')

# 集合

languages = {'c', 'java', 'ruby', 'java'}
print(languages)  # {'c', 'ruby', 'java'}

alien_0 = {'color': 'green', 'point': 5}
alien_1 = {'color': 'green', 'point': 6}
alien_2 = {'color': 'green', 'point': 7}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    if alien['point'] == 5:
        alien['color'] = 'red'
        alien['point'] = 10

print(aliens)

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

for topping in pizza['toppings']:
    print('\t' + topping)


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
