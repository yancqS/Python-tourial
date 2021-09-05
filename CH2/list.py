students = ['Tom', 'jack', 'kevin', 'Eric']
print(students)  # ['Tom', 'jack', 'kevin', 'Eric']

# 修改
students[1] = 'Eva'
print(students)  # ['Tom', 'Eva', 'kevin', 'Eric']

# 末尾添加元素
students.append('Cat')
print(students)  # ['Tom', 'Eva', 'kevin', 'Eric', 'Cat']

# 插入元素
students.insert(1, 'snake')
print(students)  # ['Tom', 'snake', 'Eva', 'kevin', 'Eric', 'Cat']

# 删除元素：del语句删除
del students[0]
print(students)  # ['snake', 'Eva', 'kevin', 'Eric', 'Cat']

# 删除元素：pop()方法删除末尾元素
popped_student = students.pop()
print(popped_student)  # Cat
print(students)  # ['snake', 'Eva', 'kevin', 'Eric']

# pop弹出列表中任何位置的元素
second_student = students.pop(1)
print(f'The second student is { second_student }')
print(students)  # ['snake', 'kevin', 'Eric']

# 根据值删除元素
students.remove('kevin')
print(students)  # ['snake', Eric']

fake_student = 'snake'
students.remove(fake_student)
print(f"{ fake_student } isn't a student")
print(students)  # ['Eric']

# 使用sort()方法对列表永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)  # ['audi', 'bmw', 'subaru', 'toyota']

# 相反的顺序排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)  # ['toyota', 'subaru', 'bmw', 'audi']

# 使用函数sorted()对列表临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))  # ['audi', 'bmw', 'subaru', 'toyota']
print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars, reverse=True))  # ['toyota', 'subaru', 'bmw', 'audi']

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']
print(cars.reverse())  # ['subaru', 'toyota', 'audi', 'bmw']

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))  # 4
