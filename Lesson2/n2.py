listCount = int(input("Сколько будет элементов списка: "))
my_list = []
i = 0
el = 0
while i < listCount:
    my_list.append(input("Введите каждый элемент списка (целые числа): "))
    i += 1
for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)