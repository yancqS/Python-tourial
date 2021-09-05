## 列表简介

### 列表是什么

**列表**由一系列特定顺序排列的元素组成，元素之间可以没有任何关系。在Python中，用方括号(`[]`)表示列表，并用逗号分割其中的元素。

```Python
letters = ['a', 'b', 'c']
print(letters) # ['a', 'b', 'c']
```

#### 访问/使用列表中的元素

列表是有序集合，因此要访问列表中的任何元素，只要将该元素的位置（索引）告诉python即可。

```Python
letters = ['a', 'b', 'c']
print(letters[0]) # a
print(letters[0].upper()) # A
print(letters[-1]) # c
print(letters[-2]) # b
message = f'The first letter is { letters[0] }'
print(message) # The first letter is a
```

#### 修改、添加和删除元素

```Python
students = ['Tom', 'jack', 'kevin', 'Eric']
print(students) # ['Tom', 'jack', 'kevin', 'Eric']

# 修改
students[1] = 'Eva'
print(students) # ['Tom', 'Eva', 'kevin', 'Eric']

# 末尾添加元素
students.append('Cat')
print(students) # ['Tom', 'Eva', 'kevin', 'Eric', 'Cat']

# 插入元素
students.insert(1, 'snake')
print(students) # ['Tom', 'snake', 'Eva', 'kevin', 'Eric', 'Cat']

# 删除元素：del语句删除
del students[0]
print(students) # ['snake', 'Eva', 'kevin', 'Eric', 'Cat']

# 删除元素：pop()方法删除末尾元素
popped_student = students.pop()
print(popped_student) # Cat
print(students) # ['snake', 'Eva', 'kevin', 'Eric']

# pop弹出列表中任何位置的元素
second_student = students.pop(1)
print(f'The second student is { second_student }')
print(students) # ['snake', 'kevin', 'Eric']

# 根据值删除元素
students.remove('kevin')
print(students) # ['snake', Eric']

fake_student = 'snake'
students.remove(fake_student)
print(f"{ fake_student } isn't a student") # snake isn't a student
print(students) # ['Eric']
```

>方法`remove()`只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要循环来确保每个值都删除。

### 组织列表

#### 列表排序

```Python
# 使用sort()方法对列表永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) #  ['audi', 'bmw', 'subaru', 'toyota']

# 相反的顺序排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars) #  ['toyota', 'subaru', 'bmw', 'audi']

# 使用函数sorted()对列表临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) #  ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars)) #  ['audi', 'bmw', 'subaru', 'toyota']
print(cars) # ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars, reverse=True)) #  ['toyota', 'subaru', 'bmw', 'audi']
```

#### 反转列表元素

反转列表排列顺序，可使用方法`reverse()`

```Python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) #  ['bmw', 'audi', 'toyota', 'subaru']
print(cars.reverse()) #  ['subaru', 'toyota', 'audi', 'bmw']
```

方法`reverse()`也是永久性修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，只需要对列表再次调用`reverse()`方法即可。

#### 确定列表长度

`len()`函数可获得列表长度。

```Python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars)) #  4
```