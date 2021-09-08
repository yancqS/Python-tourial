## 操作列表

### 遍历列表

```Python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
print('That was a great magic show')

# 输出为
alice
david
carolina
That was a great magic show
```

>注意缩进&**不要遗忘冒号**

### 创建数字列表

#### range()函数

Python函数`range()`可以生成一系列数。比如：

```Python
for value in range(1, 5):
    print(value)

# 输出结果为：
1
2
3
4
```

>左闭右开，很多语言都是这个样子。

#### 使用range()函数创建数字列表

要创建数字列表，可使用函数`list()`将`range()`的结果直接转换为列表。

```Python
numbers = list(range(1, 6))
print(numbers) #  [1, 2, 3, 4, 5]

# range() 指定一个参数
numbers = list(range(6))
print(numbers) #  [0， 1, 2, 3, 4, 5]

# range() 第三个参数指定步长
numbers = list(range(0, 6, 2))
print(numbers) #  [0，2, 4]

print(list(range(6, 2))) #  []
```

有几个专门用于处理数字列表的python函数：

- `min(list)` 找出数字列表中最小值
- `max(list)` 找出数字列表中最大值
- `sun(list)` 数字列表总和


#### 列表解析

列表解析将for循环和创建新元素的代码合并到一行，并自动附加新元素。

```Python
# 列表解析
squares = [value ** 2 for value in range(1, 11)]
print(squares) #  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 等价于
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### 切片

我们已经知道如何访问单个列表元素，以及处理列表的所有元素。除此之外，我们还可以处理列表部分，python称之为**切片**。

要创建切片，可指定要使用的第一个元素和最后一个元素的索引。

```Python
players = ['charles', 'martina', 'michnel', 'florance', 'eli']

print(players[0:3])  # ['charles', 'martina', 'michnel']

print(players[:4])  #  ['charles', 'martina', 'michnel', 'florance']

print(players[:4:2])  # ['charles', 'michnel']

print(players[2:])  # ['michnel', 'florance', 'eli']

print(players[-3:])  # ['michnel', 'florance', 'eli']

print(players[: -3])  # ['charles', 'martina']

print(players[:])  # ['charles', 'martina', 'michnel', 'florance', 'eli']
```

如果没有指定起始索引，python从列表开头开始提取；如果省略终止索引,切片终止于列表末尾。

可在切片的方括号内指定第三个值，来告诉python在指定范围内每隔多少元素提取一个。

#### 遍历切片 & 复制列表

```Python
players = ['charles', 'martina', 'michnel', 'florance', 'eli']

for play in players[:3]:
    print(play.title())

# 输出：
Charles
Martina
Michnel
```

复制列表

```Python
my_foods = ['pizza', 'falafel', 'carrot cake']

frineds_foods = my_foods[:] #  深拷贝
other_friend = my_foods #  浅拷贝

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
```

输出为：

```Python
my_foods: ['pizza', 'falafel', 'carrot cake']
frineds_foods: ['pizza', 'falafel', 'carrot cake']
other_friend: ['pizza', 'falafel', 'carrot cake']
----------------------------------------
my_foods: ['pizza', 'falafel', 'carrot cake', 'ice cream', 'dumpling']
frineds_foods: ['pizza', 'falafel', 'carrot cake', 'cannoli']
other_friend: ['pizza', 'falafel', 'carrot cake', 'ice cream', 'dumpling']
```

### 元组

列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修该的。然而，有时候你需要创建一系列不可修改的元素，**元组**可以满足这种需求。

#### 定义元组 & 遍历元组

元组看起来很像列表，但使用圆括号而非中括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表一样。

```Python
dimensions = (200, 50)
print(dimensions[0])  # 200
print(dimensions[1])  # 50

# dimensions[0] = 300 #  会导致python报错 TypeError: 'tuple' object does not support item assignment
```

>严格来说，元组是由逗号标识的，圆括号只是让元组看起来更加整洁、更清晰。如果要定义只包含一个元素的元组，必须在这个元素的后面加上逗号：
>`mt_t = (3,)`

遍历元组：

```Python
dimensions = (200, 50)

for dimension in dimensions:
    print(dimension)
```

和遍历列表一样。

#### 修改元组变量

虽然不能修改元组的元素，但是可以给存储元组的变量赋值。

```Python
dimensions = (100, 200)

dimensions = (200, 400)
```