import random


class Car:
    speed = 50
    color = "красная"
    name = "лада гранта"
    is_police = False

    def go_func(self, speed, color, name):
        print("Машина", color, name, "поехала со скоростью", speed, "км/ч")

    def stop_func(self, color, name):
        print("Машина", color, name, "стоит на месте")

    def turn_func(self, color, name):
        direction = ["прямо", "влево", "вправо"]
        print("Машина", color, name, "повернула в направлении", random.choice(direction))

    def show_speed(self, speed, color, name):
        print(f'Машина {color} {name} едет со скоростью {speed} км/ч')

    def what_kind_is_it(self, is_police):
        if is_police == True:
            print(f'Это полицейские машины')
        else:
            print(f'Это не полицейские машины')

class TownCar(Car):

    def show_speed(self, speed):
        if speed > 60:
            print(f'Вы превышаете скорость!')
        else:
            print(f'Вы не превышаете скорость!')

class SportCar(Car):
    def show_speed(self, speed):
        if speed > 120:
            print(f'Вы превышаете скорость!')
        else:
            print(f'Вы не превышаете скорость!')

class WorkCar(Car):
    def show_speed(self, speed):
        if speed > 40:
            print(f'Вы превышаете скорость!')
        else:
            print(f'Вы не превышаете скорость!')

class PoliceCar(Car):
    is_police = True

print(f'\n***TOWN CAR***\n')

tc = TownCar()
tc.go_func(40, "желтая", "лада веста")
tc.stop_func("синяя", "лада ларгус")
tc.turn_func("зеленая", "лада иксрей")
tc.show_speed(55)

print(f'\n***SPORT CAR***\n')

sc = SportCar()
sc.go_func(200, "серебристый металлик", "ферари")
sc.stop_func("золотистый металлик", "додж")
sc.turn_func("платиновый металлик", "альпин")
sc.show_speed(220)

print(f'\n***WORK CAR***\n')

wc = WorkCar()
wc.go_func(40, "синий", "трактор")
wc.stop_func("белая", "карета скорой помощи")
wc.turn_func("красная", "пожарная машина")
wc.show_speed(90)

print(f'\n***POLICE CAR***\n')

pc = PoliceCar()
pc.go_func(40, "черная", "лада веста")
pc.stop_func("черная", "лада ларгус")
pc.turn_func("черная", "лада иксрей")
pc.show_speed(145, "черная", "волга")
pc.what_kind_is_it(True)