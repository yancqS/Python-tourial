def greet(user_name):
    print(f'hello, {user_name.title()}')


greet('jesse')

##########################################################################

# 传递参数-位置实参


def des_pet(animal_type, pet_name):
    print(f'\nI have a {animal_type}')
    print(f"My {animal_type}'s name is {pet_name}")


des_pet('dog', 'Tom')


# 传递参数-关键字实参


def des_pet(animal_type, pet_name):
    print(f'\nI have a {animal_type}')
    print(f"My {animal_type}'s name is {pet_name}")


des_pet(pet_name='Tom', animal_type='dog')

##########################################################################

# 默认值


def des_pet(pet_name, animal_type='dog'):
    print(f'\nI have a {animal_type}')
    print(f"My {animal_type}'s name is {pet_name}")


des_pet('Tom')
des_pet(pet_name='Tom', animal_type='Cat')
des_pet('Tom', 'Cat')
des_pet(animal_type='CCC', pet_name='Toom')
des_pet('CCC', animal_type='Toom')

##########################################################################

# 返回值


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


def build_person(first_name, last_name, age=None):
    """可将None视为占位值。在条件测试中。None相当于False"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


print(build_person("tom", "john"))
print(build_person("tom", "john", 27))

##########################################################################

# 传递列表


def print_model(unprintdesign, printeddesign=[]):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    :param unprintdesign:
    :param printeddesign:
    :return:
    """
    while unprintdesign:
        current_design = unprintdesign.pop()
        print(f'Printing Model is: {current_design}')
        printeddesign.append(current_design)


def show_printed_model(printeddesign):
    """
    显示打印好的所有模型
    :param printeddesign:
    :return:
    """
    print(f'\nThe following model have been printed:\n')
    for design in printeddesign:
        print(design)


un_print_design = ['phone case', 'robot case', 'other case']
printed_design = []

print_model(un_print_design, printed_design)
show_printed_model(printed_design)

##########################################################################

# 传递任意数量的实参


def pizza(*toppings):
    print(toppings)


pizza('a', 'b', 'c')  # ('a', 'b', 'c')


def pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


pizza(16, 'a', 'b', 'c')

# 使用任意数量的关键字实参


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princton', field='physics')
print(user_profile)
