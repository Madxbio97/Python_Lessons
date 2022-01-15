class Road:

    def __init__(self, lenght, width, value):
        self._lenght = lenght
        self._width = width
        self._value = value

    def my_func(self):
        print("Длина:", self._lenght, "(м)", "Ширина:", self._lenght, "(м)", "Вес:", self._value, "(кг)", "\n")
        my_formula = self._lenght * self._lenght * self._value
        print("Нужно асфальта:", my_formula, "(кг)", "или", my_formula / 1000, "(т)")

r = Road(28, 29, 40)
r.my_func()