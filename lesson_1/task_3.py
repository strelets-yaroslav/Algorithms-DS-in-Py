"""3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно."""

from random import randint, uniform

print('Введите границы диапазона для генерации случайного целого числа.')
int_from = int(input('левая граница: '))
int_to = int(input('правая граница: '))

print('Введите границы диапазона для генерации случайного вещественного числа.')
float_from = float(input('левая граница: '))
float_to = float(input('правая граница: '))

print('Введите границы диапазона для генерации случайного символа.')
char_from = ord(input('левая граница: ').lower())
char_to = ord(input('правая граница: ').lower())

rand_int = randint(min(int_from, int_to), max(int_from, int_to))
rand_float = uniform(min(float_from, float_to), max(float_from, float_to))
rand_char = chr(randint(min(char_from, char_to), max(char_from, char_to)))

print(f'Случайное целое число: {rand_int}')
print(f'Случайное вещественное число: {rand_float}')
print(f'Случайный символ: {rand_char}')
