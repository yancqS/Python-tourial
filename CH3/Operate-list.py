magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
print('That was a great magic show')

for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)  # [1, 2, 3, 4, 5]
print(min(numbers))  # 1
print(max(numbers))  # 5
print(sum(numbers))  # 15

# range() 指定一个参数
numbers = list(range(6))
print(numbers)  # [0， 1, 2, 3, 4, 5]

# range() 第三个参数指定步长
numbers = list(range(0, 6, 2))
print(numbers)  # [0，2, 4]

print(list(range(6, 2)))  # []

# 列表解析
squares = [value ** 2 for value in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 等价于
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

players = ['charles', 'martina', 'michnel', 'florance', 'eli']

print(players[0:3])  # ['charles', 'martina', 'michnel']

print(players[:4])  # ['charles', 'martina', 'michnel', 'florance']

print(players[:4:2])  # ['charles', 'michnel']

print(players[2:])  # ['michnel', 'florance', 'eli']

print(players[-3:])  # ['michnel', 'florance', 'eli']

print(players[: -3])  # ['charles', 'martina']

print(players[:])  # ['charles', 'martina', 'michnel', 'florance', 'eli']

players = ['charles', 'martina', 'michnel', 'florance', 'eli']

for play in players[:3]:
    print(play.title())

my_foods = ['pizza', 'falafel', 'carrot cake']

frineds_foods = my_foods[:]  # 深拷贝
other_friend = my_foods  # 浅拷贝

print('my_foods:', my_foods)
print('frineds_foods:', frineds_foods)
print('other_friend:', other_friend)

my_foods.append('ice cream')
frineds_foods.append('cannoli')
other_friend.append('dumpling')

print('-' * 40)

print('my_foods:', my_foods)
print('frineds_foods:', frineds_foods)
print('other_friend:', other_friend)

dimensions = (200, 50)
print(dimensions[0])  # 200
print(dimensions[1])  # 50

# dimensions[0] = 300 #  会导致python报错 TypeError: 'tuple' object does not support item assignment

dimensions = (200, 50)

for dimension in dimensions:
    print(dimension)

dimensions = (100, 200)

dimensions = (200, 400)
