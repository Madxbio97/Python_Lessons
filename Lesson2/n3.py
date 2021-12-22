#реализация с помощью списка:
userInput = int(input("Введите номер месяца: "))
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
for i in winter:
    if userInput == i:
        print(userInput, "месяц - это зима")
for i in spring:
    if userInput == i:
        print(userInput, "месяц - это весна")
for i in summer:
    if userInput == i:
        print(userInput, "месяц - это лето")
for i in autumn:
    if userInput == i:
        print(userInput, "месяц - это осень")

#реализация с помощью словаря:
seasons = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
userInput = int(input("Введите номер месяца: "))
if userInput ==12 or userInput == 1 or userInput == 2:
        print(userInput, "месяц - это", seasons.get(1))
elif userInput == 3 or userInput == 4 or userInput ==5:
    print(userInput, "месяц - это", seasons.get(2))
elif userInput == 6 or userInput == 7 or userInput == 8:
    print(userInput, "месяц - это", seasons.get(3))
elif userInput == 9 or userInput == 10 or userInput == 11:
    print(userInput, "месяц - это", seasons.get(4))