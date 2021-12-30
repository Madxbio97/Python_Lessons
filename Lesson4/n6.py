from itertools import count
from itertools import cycle

new_iteration = count(start=int(input()), step=1)

for i in new_iteration:
    if i == 10:
        break
    print(new_iteration)

с = 0
for el in cycle("ABC"):
    if с > 10:
        break
    print(el)
    с += 1
