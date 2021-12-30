my_list = [2, 4, 6, 10, 8, 7, 100]
new_list = []
for i in range(len(my_list)-1):
    if my_list[i] < my_list[i+1]:
        new_list.append(my_list[i+1])

print(new_list)