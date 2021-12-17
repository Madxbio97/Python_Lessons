a = abs(int(input("Введите ваше число: ")))
maximum = a % 10
while a >= 1:
    a = a // 10
    if a % 10 > maximum:
        maximum = a % 10
    if a > 9:
        continue
    else:
        print("Максимальное положительное число: ", maximum)
        break