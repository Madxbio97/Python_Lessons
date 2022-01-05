def userInput():
    out_f = open("n5.txt", "w+")
    nums = input("Введите цифры через пробел: ")
    out_f.writelines(nums)
    final = nums.split()
    print(sum(map(int, final)))
    out_f.close()
userInput()