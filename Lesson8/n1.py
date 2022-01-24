class Date:
    user_date = str("12/12/2021")

    @classmethod
    def user_date_to_numeric(self, user_date):
        my_date_list = []
        for i in user_date.split("/"):
            if i != "/":
                my_date_list.append(i)
        return int(my_date_list[0]), int(my_date_list[1]), int(my_date_list[2])

    @staticmethod
    def validate_user_date(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if year > 0:
                    return f'Текущая дата: {day}/{month}/{year}'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'


print(f'Текущая дата в числовом выражении: {Date.user_date_to_numeric("12/12/2021")}')
d = Date()
print(d.validate_user_date(1, 13, 2022))