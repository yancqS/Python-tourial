## 第十章 文件和异常

### 从文件中读取数据

新建一个文件`pi_digits.txt`,他包含精确到小数点后30位的圆周率值，且在小数点后10位处换行：

```
3.1415926535
  8979323846
  2463383297
```

 下面的程序打开并读取这个文件，再将其显示在屏幕上：

```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents)
```

函数`open()`返回一个表示文件的对象。在本例中，`open('pi_digits.txt')`返回一个表示文件`pi_digits.txt`的对象，Python将该对象赋给`file_object`供以后使用。

关键字`with`在不需要访问文件后将其关闭。在这程序中调用了`open()`方法，但是没有调用`close()`方法。也可以调用`open()`和`close()`方法，但这样做时，如果程序存在bug导致方法`close()`未执行，文件将不会关闭。未妥善关闭的文件可能会导致数据丢失。如果在程序执行过程中过早的调用`clsoe()`方法，会发现在需要使用文件时它已关闭，这会导致更多的错误。但是使用`with`可以让Python去确定：你只管打开文件，并在需要时使用它，Python自会在合适的时候自动将其关闭。

然后使用`read()`方法读取这个文件的全部内容，并将其作为一个长长的字符串赋给变量`contents`。

#### 逐行读取

```python
file_name = "pi_digits.txt"

with open(file_name) as file_object_line:
    for line in file_object_line:
        print(line.rstrip())
```

#### 创建一个包含文件各行内容的列表

```python
file_name = "pi_digits.txt"

with open(file_name) as file_object_rline:
    lines = file_object_rline.readlines()

print(lines) # ['3.1415926535\n', '  8979323846\n', '  2463383297']

for line in lines:
    print(line.rstrip())
```

#### 使用文件内容

```py
file_name = "pi_digits.txt"

with open(file_name) as file_object_rline:
    lines = file_object_rline.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string) # 3.141592653589793238462463383297
print(len(pi_string)) # 32
```

注意：读取文本文件时，Python将其中的所有文本都解读为字符串。如果读取的时数，并要将其作为数字使用，就必须使用函数`int()`将其转换为整数或使用函数`float()`将其转换为浮点数。

### 写入文件

#### 写入空文件

要将文本写入文件，在调用`open()`时需要提供另一个实参，告诉Python你要写入打开的文件。

```python
file_name_w = 'pi.txt'

with open(file_name_w, 'w') as file_object_w:
    file_object_w.write('I love programming')
```

在本例中，调用`open()`时提供了两个实参。第一个仍然是要打开的文件名称。第二个实参('w')告诉Python，要以**写入模式**打开这个文件。如果要写入的文件不存在，函数`open()`会自动创建它。

> 打开文件时，可指定读取模式('r')、写入模式('w')、附加模式('a')或读写模式('r+')。如果省略模式实参，Python将以默认的只读模式打开文件

> Python只能将字符串写入文本文件，要将数值数据存储到文本文件中，必须先试用`str()`将其转换为字符串格式。

#### 写入多行&附加到文件

```python
# 写入多行
file_name_w = 'pi.txt'

with open(file_name_w, 'w') as file_object_w:
    file_object_w.write('I love programming\n')
    file_object_w.write('I love programming too\n')

# 附加到文件
    
with open(file_name_w, 'a') as file_object_a:
    file_object_a.write('I also love finding meaning in large dataset.\n')
    file_object_a.write('I also love finding meaning in large dataset too.\n')
```

此时`pi.txt`的内容为：

```
I love programming
I love programming too
I also love finding meaning in large dataset.
I also love finding meaning in large dataset too.

```

### 异常

Python使用称为**异常**的特殊对象来管理程序执行期间发生的错误。异常时使用`try-except`代码块处理的，即便出现异常，程序也将继续运行：显示你编写的友好的提示信息。

例如：

```python
try:
    print(5/0)
except ZeroDivisionError:
    print('You can not divide by zero')
```

> `5/0`Python会抛出`ZeroDivisionError`错误对象。

如果`try`代码块运行起来没有问题，Python将会跳过`except`代码块。

#### else代码块

依赖`try`代码块成功执行的代码都应该放到else代码块中。

```py
print('Give me two number, and I will divede them')
print('Enter q to quit')

while True:
    first_num = input('\nFirst num: ')
    if first_num == 'q':
        break

    second_num = input('Second num: ')
    if second_num == 'q':
        break

    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print('You can not divide by zero')
    else:
        print(answer)
```

#### 处理FileNotFoundError异常

```python
file_name = 'alice.txt'
try:
    with open(file_name, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print('File Not Found')
```

#### 分析文本

方法`split()`默认以空格为分隔符将字符串分拆为对个部分，并将这些部分存储到一个列表中。

假如我们想分析一篇文章包含多少个单词，我们可以这么做：

```python
file_name = 'pi.txt'
try:
    with open(file_name, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print('File Not Found')
else:
    print(f"The file has about {len(content.split())} words")
```

#### 静默失败

Python有一个`pass`语句，可用于让Python在代码块中什么也不要做；此外`pass`语句还充当占位符，提醒你在程序中的某个地方什么都没做，并且以后也许要在这个地方做些什么。

```python
file_name = 'pi3.txt'
try:
    with open(file_name, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    pass
else:
    print(f"The file has about {len(content.split())} words")
```

### 存储数据

模块`json`让你可以能够将简单的Python数据结构转储到文件中，并在程序再次运行时加载这些文件中的数据。

#### 使用 json.dump() 和 json.load()

我们来编写一个存储一组数的简单的程序，在编写一个将这些数读取到内存的程序。第一个程序将使用`json.dump()`来存储数据，而第二个程序将使`json.load()`。

```python
import json
number = [1, 2, 3, 4, 5]

file_name = 'number.json'

with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(number, f)

with open(file_name, encoding='utf-8') as f_r:
    r_number = json.load(f_r)

print(r_number)
```

#### 保存和读取用户生成的数据

```python
file_name = 'username.json'

try:
    with open(file_name) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input('Input your name: ')
    with open(file_name, 'w') as f_w:
        json.dump(username, f_w)
        print(f'we will remember you when you basck, {username}')
else:
    print(f'welcom back, {username}')
```