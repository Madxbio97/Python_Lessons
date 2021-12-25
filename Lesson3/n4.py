def my_func1(x, y):
    print (x ** y)
my_func1(x = int(input("Введите целое положительное число: ")), y = int(input("Введите целое отрицательное число: ")))

def my_func2(x, y):
    check = 1
    result = 1 / x
    while check < abs(y):
        check += 1
        print(result * (1 / x))
my_func2(x = int(input("Введите целое положительное число: ")), y = int(input("Введите целое отрицательное число: ")))
