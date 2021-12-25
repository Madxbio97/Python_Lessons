def myFunc(a = int(input()), b = int(input())):
    if b == 0:
        print("Ошибка ввода: делить на ноль нельзя")
    else:
        c = a // b
        print(c)
myFunc()