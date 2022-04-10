"""1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за четыре квартала для каждого предприятия. Программа должна определить
среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего."""

from collections import namedtuple, deque

n, q = 0, 4
err_str = 'Введено некорретное значение! Попробуйте снова.'
company_fields = ['name', 'quarter_profit', 'year_profit']
companies = deque()
less_income = deque()
big_income = deque()

while True:
    try:
        n = int(input('Введите количество предприятий: '))
        if n > 0:
            break
    except ValueError:
        pass
    print(err_str)

mean_profit = 0
for i in range(n):
    company = namedtuple('company', company_fields)
    company.name = input(f'Введите название {i + 1}-го предприятия: ')

    profit_str = 'Введите поквартальный доход за год через пробел: '
    while True:
        try:
            company.quarter_profit = [float(item) for item in input(profit_str).split()]
            if len(company.quarter_profit) == q:
                break
        except ValueError:
            pass
        print(err_str)

    company.year_profit = sum(company.quarter_profit)
    mean_profit += company.year_profit
    companies.append(company)

mean_profit /= n

[(less_income, big_income)[company.year_profit >= mean_profit].append(company) for company in companies]

print(f'Средний годовой доход по предприятиям составил {mean_profit}.')
print('Предприятия с доходом больше среднего:')
for company in big_income:
    print(f'{company.name} с доходом {company.year_profit}')

print('Предприятия с доходом меньше среднего:')
for company in less_income:
    print(f'{company.name} с доходом {company.year_profit}')
