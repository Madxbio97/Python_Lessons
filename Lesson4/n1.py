from sys import argv

hours_production = argv
rate_per_hour = argv
bonus = argv

print("Выработка в часах: ", hours_production)
print("Ставка в час: ", rate_per_hour)
print("Премия: ", bonus)
print("Зарплата сотрудника: ", (int(hours_production) * int(rate_per_hour)) + int(bonus))