## 第八章 函数

### 定义函数

```Python
def greet(user_name):
    print(f'hello, {user_name.title()}')


greet('jesse')
```

关键字 `def` 来定义函数，向Python指出了函数名，还会在圆括号内指出函数为完成任务需要什么样的信息，即使不需要信息也不可以省略，最后定义以冒号结尾。紧跟在 `def greet():` 后面的所有缩进行构成了函数体。

函数定义中的变量称为*形参*，函数调用中的变量称为*实参*。

### 传递参数

向函数传递实参的方式有很多：可使用**位置实参**，这要求实参的顺序和形参的顺序相同；也可以使用**关键字实参**，其中每个实参都由变量名和值组成；还可以使用列表和字典。

- 位置实参

```Python
def des_pet(animal_type, pet_name):
    print(f'\nI have a {animal_type}')
    print(f"My {animal_type}'s name is {pet_name}")


des_pet('dog', 'Tom')
```

- 关键字实参

```Python
def des_pet(animal_type, pet_name):
    print(f'\nI have a {animal_type}')
    print(f"My {animal_type}'s name is {pet_name}")


des_pet(pet_name='Tom', animal_type='dog')
```

### 默认值

```Python
def des_pet(pet_name, animal_type='dog'):
    print(f'\nI have a {animal_type}')
    print(f"My {animal_type}'s name is {pet_name}")


des_pet('Tom')
des_pet(pet_name='Tom', animal_type='Cat')
des_pet('Tom', 'Cat')
des_pet(animal_type='CCC', pet_name='Toom')
des_pet('CCC', animal_type='Toom')
```

### 返回值

在函数中，可使用`return`语句将值返回调用函数的代码行。返回值能让程序将大部分繁重的工作移到函数中去完成，从而简化主程序。

- 返回简单值

```Python
def format_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()


print(format_name('john', 'tom'))
print(format_name('john', 'tom', 'Selina'))
print(format_name.__doc__)
```

- 返回字典

```Python
def build_person(first_name, last_name, age=None):
    """可将None视为占位值。在条件测试中。None相当于False"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


print(build_person("tom", "john"))
print(build_person("tom", "john", 27))
```

### 传递列表

向函数传递列表很有用，其中包括的可能是名字、数或更复杂的对象（如字典）。

```python
def print_model(un_print_design, printed_design=[]):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    :param un_print_design: 
    :param printed_design: 
    :return: 
    """
    while un_print_design:
        current_design = un_print_design.pop()
        print(f'Printing Model is: {current_design}')
        printed_design.append(current_design)


def show_printed_model(printed_design):
    """
    显示打印好的所有模型
    :param printed_design: 
    :return: 
    """
    print(f'\nThe following model have been printed:\n')
    for design in printed_design:
        print(design)


un_print_design = ['phone case', 'robot case', 'other case']
printed_design = []

print_model(un_print_design, printed_design)
show_printed_model(printed_design)
```

### 传递任意数量的实参

有时候，预先不知道函数需要接受多少个实参，好在Python允许函数从调用语句中收集任意数量的实参。

```python
def pizza(*toppings):
    print(toppings)
    
    
pizza('a', 'b', 'c') # ('a', 'b', 'c')
```

形参名`*toppings`中的星号让Python创建一个名为`toppings`的空元组，并将收到的所有值都封装到这个元组中。

### 结合使用位置实参和任意数量实参

如果要让函数接受不同类型的实参，必须在函数定义中接纳任意数量实参的形参放在最后。Python先匹配位置实参和关键字实参，再将剩余的实参都收集到最后一个形参中。

```python
def pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


pizza(16, 'a', 'b', 'c')
```

### 使用任意数量的关键字实参

```python
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princton', field='physics')
print(user_profile)
```

形参名`**user_info`中的两个星号让Python创建一个名为`user_info`的空字典，并将收到的所有键值对都放到这个字典中。

### 将函数存储在模块中

我们可以将函数存储在称为**模块**的独立文件中，再将模块导入到主程序中。

- 导入整个模块

语法如下：

> import *module_name*
>
> module_name.function_name()

创建`pizza.py`文件：

```python
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
```

然后在同一目录创建一个名为`making_pizza.py`的文件。这个文件导入刚创建的模块，再调用make_pizza()两次：

```python
import pizza

pizza.make_pizza(16, 'a', 'b', 'c')
pizza.make_pizza(12, 'a', 'b')
```

- 导入特定的函数

语法如下：

> from *module_name* import *function_name1, function_name2*

上面的例子可重写为：

```python
from pizza import make_pizza

make_pizza(16, 'a', 'b', 'c')
make_pizza(12, 'a', 'b')
```

- 使用as给函数指定别名

语法如下：

> from *module_name* import *function_name* as *fn*

```python
from pizza import make_pizza as mp

mp(16, 'a', 'b', 'c')
mp(12, 'a', 'b')
```

- 使用as给模块指定别名

语法如下：

> import *module_name* as *mn*

```python
import pizza as p

p.make_pizza(16, 'a', 'b', 'c')
p.make_pizza(12, 'a', 'b')
```

- 导入模块中所有函数

语法如下：

> from *module_name* import *

```python
from pizza import *

make_pizza(16, 'a', 'b', 'c')
make_pizza(12, 'a', 'b')
```