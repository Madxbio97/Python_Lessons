d = {}
f = open('n6.txt', encoding='utf-8')
splitResult = f.read().split("\n")[:-1]
print(splitResult)

for item in splitResult:
    key = item.split(" ")[0]
    value = item.split(" ")[1:]
    d[key] = value
print(d)

for i in d:
    list = d[i]
    summ = 0
    for j in range(0, len(list)):
        summ += int(list[j])
    print(i, ":", summ)
f.close()