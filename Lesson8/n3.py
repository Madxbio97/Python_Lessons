class MyClass(ValueError):
    pass

class_list = []
while True:
    try:
        value = input('Введите число в список:')
        if value == 'q':
            break
        if not value.isdigit():
            raise MyClass(value)
        class_list.append(int(value))
    except MyClass as ex:
        print('Не число!', ex)
print(class_list)