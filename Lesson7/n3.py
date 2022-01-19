class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    @property
    def translate_quantity(self):
        return self.quantity

    def __str__(self):
        return self.quantity * "*"

    def __add__(self, other):
        return Cell(int(self.quantity + other.quantity))

    def __sub__(self, other):
        return Cell(self.quantity - other.quantity)

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, order):
        gap = ''
        for i in range(int(self.quantity / order)):
            gap += f'{"*" * order} \\n'
        gap += f'{"*" * (self.quantity % order)}'
        return gap

c1 = Cell(10)
c2 = Cell(2)
print(c1)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(f'Результат выполнения метода: {c1.make_order(10)}, {c2.make_order(2)}')
