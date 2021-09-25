import json

with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents)

##########################################################################

# 逐行读取

file_name = "pi_digits.txt"

with open(file_name) as file_object_line:
    for line in file_object_line:
        print(line.rstrip())

##########################################################################

file_name = "pi_digits.txt"

with open(file_name) as file_object_rline:
    lines = file_object_rline.readlines()

print(lines)  # ['3.1415926535\n', '  8979323846\n', '  2463383297']

for line in lines:
    print(line.rstrip())

##########################################################################

file_name = "pi_digits.txt"

with open(file_name) as file_object_rline:
    lines = file_object_rline.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string)  # 3.141592653589793238462463383297
print(len(pi_string))  # 32

##########################################################################

# 写入文件

file_name_w = 'pi.txt'

with open(file_name_w, 'w') as file_object_w:
    file_object_w.write('I love programming')

# 写入多行

with open(file_name_w, 'w') as file_object_w:
    file_object_w.write('I love programming\n')
    file_object_w.write('I love programming too\n')

# 附加到文件
with open(file_name_w, 'a') as file_object_a:
    file_object_a.write('I also love finding meaning in large dataset.\n')
    file_object_a.write('I also love finding meaning in large dataset too.\n')

##########################################################################

# 异常

try:
    print(5/0)
except ZeroDivisionError:
    print('You can not divide by zero')

# else代码块

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

# 处理FileNotFoundError异常

file_name = 'alice.txt'
try:
    with open(file_name, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print('File Not Found')

##########################################################################

# 分析文本

# 方法`split()`默认以空格为分隔符将字符串分拆为对个部分，并将这些部分存储到一个列表中

file_name = 'pi.txt'
try:
    with open(file_name, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print('File Not Found')
else:
    print(f"The file has about {len(content.split())} words")

# 静默失败

file_name = 'pi3.txt'
try:
    with open(file_name, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    pass
else:
    print(f"The file has about {len(content.split())} words")


##########################################################################

# 存储数据

# 使用 json.dump() 和 json.load()

number = [1, 2, 3, 4, 5]

file_name = 'number.json'

with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(number, f)

with open(file_name, encoding='utf-8') as f_r:
    r_number = json.load(f_r)

print(r_number)

# 保存和读取用户生成的数据

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

