profit = int(input("Введите размер прибыли: "))
cost = int(input("Введите размер издержек: "))

if profit > cost:
    print("Поздравляю, ваша фирма приносит прибыль")
    print("Рентабельность составляет: ", (profit - cost) / profit)
if cost > profit:
    print("К сожалению, ваша фирма работает в убыток")
if profit == cost:
    print("Ваша фирма работает в ноль")
workers = int(input("Введите количество работников: "))
print("Прибыль в расчете на каждого сотрудника составляет: ", profit / workers)