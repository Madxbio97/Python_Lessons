#Вносим данные
merchList = []
while input("Хотите ли вы добавить новый товар (да / нет): ") == 'да':
    number = int(input("Введите номер товара: "))
    features = {}
    while input("Хотите ли вы добавить параметры товара (да / нет): ") == 'да':
        feature_key = input("Введите характеристики товара: ")
        feature_value = input("Введите значение этой характеристики товара: ")
        features[feature_key] = feature_value
    merchList.append(tuple([number, features]))
print(merchList)

#Пишем аналитику
analysis = {}
for good in merchList:
    for feature_key, feature_value in good[1].items():
        if feature_key in analysis:
            analysis[feature_key].append(feature_value)
        else:
         analysis[feature_key] = [feature_value]
print(analysis)
