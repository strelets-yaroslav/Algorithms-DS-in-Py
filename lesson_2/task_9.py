"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр."""


def digits_sum(num):
    """возвращает сумму цифр числа"""
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s


def str_digits_sum(s_num):
    """возвращает сумму цифр в строке, представляющей число"""
    s = 0
    for s_dig in s_num:
        s += int(s_dig) if s_dig.isdigit() else 0
    return s


# не стал делать таким образом, т.к. тут массив =)
# s_numbers = input('Введите натуральные числа через пробел: ').split(' ')

num_count = int(input('Введите количество чисел для обработки: ')) + 1

max_num, max_digits_num = 0, 0
max_num1, max_digits_num1 = 0, 0
for i in range(1, num_count):
    s_number = input(f'Введите {i}-е число: ')
    number_digits_sum = digits_sum(abs(int(s_number)))
    if max_digits_num < number_digits_sum:
        max_num, max_digits_num = s_number, number_digits_sum

    number_digits_sum = str_digits_sum(s_number)
    if max_digits_num1 < number_digits_sum:
        max_num1, max_digits_num1 = s_number, number_digits_sum

print(f'Число с максимальной суммой цифр ({max_digits_num}): {max_num}')
print('\nРезультат при обработке строк:')
print(f'Число с максимальной суммой цифр ({max_digits_num1}): {max_num1}')
