while True:
    i = input(">>>")
    i = i.split(" ")
    a = 0
    while a < len(i):
        try:
            i[a] = int(i[a])
        except ValueError:
            print("Value Error")
            break
        a = a + 1
    z = 0
    for c in i:
        z = z + c
    print(z)