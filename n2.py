seconds = int(input("Введите время: "))
seconds = seconds % (24 * 3600)
hours = seconds // 3600

seconds = seconds % 3600
minutes = seconds // 60

seconds = seconds % 60
print("%02d:%02d:%02d" % (hours, minutes, seconds))