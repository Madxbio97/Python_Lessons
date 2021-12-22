#решение для очень ленивых
my_list = [7, 5, 3, 3, 2]
print(my_list)
newElement = int(input("Введите новый элемент в списке: "))
my_list.append(newElement) #добавим новый элемент
my_list.sort(reverse=True) #отсортируем список в обратном порядке
print(my_list)