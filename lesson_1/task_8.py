"""8. Вводятся три разных числа.
Найти, какое из них является средним (больше одного, но меньше другого)."""

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

if a == b or b == c or a == c:
    print('Надо вводить разные числа.')
else:
    middle = round(sum((a, b, c)) - max(a, b, c) - min(a, b, c), 8)
    print(f'Среднее из чисел: {middle}')
