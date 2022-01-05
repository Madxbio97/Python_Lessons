import json

bounty = {}
bountyGeneral = {}
new_profit = 0
profit_average = 0
i = 0

with open('n7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        bounty[name] = int(earning) - int(damage)
        if bounty.setdefault(name) >= 0:
            new_profit = new_profit + bounty.setdefault(name)
            i += 1
    if i != 0:
        profit_average = new_profit / i
        print(f'Средняя прибыли - {profit_average:.2f}')
    else:
        print(f'Фирма работает в убыток')
    bountyGeneral = {'прибыль (общая)': round(profit_average)}
    bounty.update(bountyGeneral)
    print(f'прибыль (каждой компании) - {bounty}')

with open('n7.txt', 'w') as write_js:
    json.dump(bounty, write_js)

    js_str = json.dumps(bounty)
    print(f'Итоговый файл: \n '
          f' {js_str}')