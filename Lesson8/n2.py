class MyClassExcep:

    @classmethod
    def try_to_check(self, a, b):
        if b == 0:
            print(f'Исключение - на ноль делить нельзя')
        else:
            print(f'Результат деления: {a / b}')

MyClassExcep.try_to_check(a=float(input("Введите первое число: ")), b=float(input("Введите второе число: ")))