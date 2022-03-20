"""2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""

num = int(input('Введите натуральное число: '))

even_count = 0
odd_count = 0

while num > 0:
    if (num % 10) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    num //= 10

print(f'Во введённом числе {even_count} чётных и {odd_count} нечётных цифр.')
