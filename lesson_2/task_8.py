"""8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры."""


def print_result(num, dig, dig_cnt):
    postfix = 'а' if (dig_cnt % 10 in (2, 3, 4) and (dig_cnt < 10 or dig_cnt > 20)) else ''
    print(f'Цифра {dig} встречается в числе {num} {dig_cnt} раз{postfix}.')


number = input('Введите число: ')
digit = input('Введите цифру: ')
digit_count = 0
for num_digit in number:
    digit_count += 1 if num_digit == digit else 0

print_result(number, digit, digit_count)

print('\nРезультат при проходе циклом, непосредственно используя числа.')
int_num, int_dig = abs(int(number)), int(digit)
digit_count = 0
while int_num > 0:
    digit_count += 1 if int_num % 10 == int_dig else 0
    int_num //= 10

print_result(number, int_dig, digit_count)
