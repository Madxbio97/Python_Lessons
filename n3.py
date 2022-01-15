class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus} #зачем тут нужен словарь по условию задачи?


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_position(self):
        return self.position

    def get_full_salary(self):
        return self._income['wage'] + self._income['bonus']


p = Position('Иван', 'Иванов', 'менеджер', 200000, 140000)
print("Сотрудник с именем и фамилией", p.get_full_name(), "занимает должность", p.get_position())
print("Зарплата сотрудника с именем и фамилией", p.get_full_name(), "составит", p.get_full_salary())