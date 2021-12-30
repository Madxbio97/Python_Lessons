from functools import reduce
myList = [i for i in range(100, 1000) if i % 2 == 0]
print(myList)
summa = reduce((lambda x, y: x * y), myList)
print(summa)
