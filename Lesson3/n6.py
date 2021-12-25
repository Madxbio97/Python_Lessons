def int_func(userInput = str(input("Введите слова: "))):
    print(userInput.title())
int_func()
userOutput = []
for word in input('Введите строку: ').split(' '):
    userOutput.append(int_func(word))
