def myFunc():
    with open('n3.txt', 'r', encoding='utf-8') as f:
        workers = {}
        for line in f:
            name, salary = line.split()
            workers[name] = name
            if int(salary) < 20000:
                print(f'{name}: зарплата меньше 20000')
        f.close()
myFunc()
