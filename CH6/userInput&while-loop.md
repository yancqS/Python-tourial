## 第七章 用户输入和while循环

### 函数input()的工作原理

函数 `input()` 让程序暂停运行，等待用户输入一下文本，获取用户输入后，Python将其赋给一个变量，以方便使用。

```Python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

### 使用int()来获取数值输入

使用函数 `input()` 时，Python将用户输入解读为字符串。

```Python
message = input("Tell me something, and I will repeat it back to you: ")
print(message > 18)
```

假如输入为数字20，但 `input()` 函数返回的是'21'，因此这样比较与数字18的大小就会报错：

```
TypeError: '>' not supported between instances of 'str' and 'int'
```

为了解决这个问题，可以使用 `int()` 函数，将数的字符串表示转换为数值表示。

```Python
message = int(input("Tell me something, and I will repeat it back to you: "))
print(message > 18) #  True
```

求模运算符（`%`）,它将两个数想除并返回余数。

```Python
4 % 3 # 1
5 % 3 # 2
6 % 3 # 0
7 % 3 # 1 
```

### while 循环

for循环用于针对集合中的每个元素都执行一个代码块。而while循环则不断执行，直到指定的条件不满足为止。

```python
current_num = 0
while current_num <= 5:
    print(current_num)
    current_num += 1
```

让用户选择何时退出, 可以使用 `while` 循环让程序在用户愿意时不断执行：

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""

while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)
```

或者可以使用**标志(flag)**:

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True

while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)
```

#### break & continue

要立即退出while循环，不再运行循环中余下的代码，也不管条件测试的结果如何，可使用 `break` 语句。

```Python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True

while active:
    message = input(prompt)
    if message == "quit":
        break
    else:
        print(message)
```

要返回循环开头，并根据条件测试结果决定是否继续执行循环，可使用 `continue` 语句，它不像 `break` 语句那样不再执行余下的代码并退出整个循环。

```Python
current = 0

while current <= 10:
    current += 1
    if current % 2 != 0:
        continue

    print(current)
```

### 使用while循环处理列表和字典

for循环是一种遍历列表的有效方式，但不应该在for循环中修改列表，否则将导致Python难以跟踪其中的元素。要在遍历列表的同时对其进行修改，可以使用while循环。

```Python
# 在列表之间移动元素

unconfirmed_user = ['alice', 'brain', 'candace']
confirmed_user = []

while unconfirmed_user:
    current_user = unconfirmed_user.pop()

    print(f'Verifying user: {current_user.title()}')
    confirmed_user.append(current_user)

print('\nThe following users have been confirmed:')
for user in reversed(confirmed_user):
    print(user.title())
```

输出为：

```
Verifying user: Candace
Verifying user: Brain
Verifying user: Alice

The following users have been confirmed:
Alice
Brain
Candace
```

```Python
# 删除为特定值的所有列表元素

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```

输出为：

```
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']
```

```Python
# 使用用户输入填充字典

responses = {}

polling = True

while polling:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
```

输出为：

```
What is your name? Tom
Which mountain would you like to climb someday? 泰山
Would you like to let another person respond? (yes/no) yes

What is your name? Jack
Which mountain would you like to climb someday? 华山
Would you like to let another person respond? (yes/no) no

--- Poll Results ---
Tom would like to climb 泰山.
Jack would like to climb 华山.
```