"""3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843."""

str_num = input('Введите число: ')
num = int(str_num)
reversed_num = 0

while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10

print(f'Число в обратном порядке: {reversed_num}')

print(f'Запрещённый для данного урока способ без заморочек =) : {str_num[::-1]}')
