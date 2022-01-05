def myFunc():
    out_f = open("n2.txt", "r")
    content = out_f.readlines()
    print("Количество строк:", len(content))
    for i in range(len(content)):
        new_l = content[i].split()
        print("Количество слов в строке:", len(new_l))
    out_f.close()
myFunc()