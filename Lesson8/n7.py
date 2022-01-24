class Complex:

    def __init__(self, first_num, second_num, complex_part):
        self.first_num = first_num
        self.second_num = second_num
        self.complex_part = complex_part

    def my_summ(self):
        print(f'Первая переменная: {self.first_num} + {self.first_num}{self.complex_part}')
        print(f'Вторая переменная: {self.second_num} + {self.second_num}{self.complex_part}')
        first_part = self.first_num + self.second_num
        print(f'Сумма двух комплексных чисел = {first_part} + {first_part}{self.complex_part}')

    def my_multiple(self):
        first_part = self.first_num * self.second_num
        print(f'Произведение двух комплексных чисел = {first_part} + {first_part}{self.complex_part}')

a = Complex(1, 2, "j")
a.my_summ()
a.my_multiple()

print("\n")

b = Complex(12.5, 28.9, "i")
b.my_summ()
b.my_multiple()