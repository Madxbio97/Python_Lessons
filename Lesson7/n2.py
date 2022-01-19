class Dress:
    name = "одежда"
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def translate_my_values(self):
        return  f"Параметры, переданные в класс:" \
            f" {self.v}, {self.h}"

    def calculate_size(self, v, h):
        print(v, h)

class Smoking(Dress):
    def calculate_size(self, v):
        name = "костюм"
        size = v / 6.5 + 0.5
        print(f'Нужно ткани для типа "{name}": {size}')

class Trench(Dress):
    def calculate_size(self, h):
        name = "пальто"
        size = 2 * h + 0.3
        print(f'Нужно ткани для типа "{name}": {size}')

s = Smoking(1, 2)
s.calculate_size(6.5)

t = Trench(3, 4)
t.calculate_size(7)