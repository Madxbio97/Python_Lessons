class Stationery:
    title = "Название"

    def draw(self, title):
        print(f'Начался запуск отрисовки с помощью {title}')

class Pen(Stationery):
    def draw(self, title):
        print(f'Для письма лучше всего подходит {title}')

class Pencil(Stationery):
    def draw(self, title):
        print(f'{title} хорош для простых чертежей')

class Handle(Stationery):
    def draw(self, title):
        print(f'{title} используют для пометок')

p = Pen()
p.draw("ручка")

pl = Pen()
pl.draw("карандаш")

pl = Handle()
pl.draw("маркер")