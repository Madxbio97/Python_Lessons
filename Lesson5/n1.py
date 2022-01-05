def userInput():
    out_f = open("n1.txt", "w")
    out_f.write(input("Введите построчно данные: "))
    out_f.close()
userInput()