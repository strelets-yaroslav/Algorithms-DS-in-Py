"""5. Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке."""


def print_ascii_table(first, last, n=10):
    res = ''
    for i in range(n):
        symbol_code = first + i
        if symbol_code > last:
            return res
        res += f'{symbol_code:>3} - {chr(symbol_code):<4}'
    return res + '\n' + print_ascii_table(first + n, last, n)


start, finish, n = 32, 127, 10

print('Таблица с помощью рекурсии:')
print(print_ascii_table(start, finish, n))

print('\nТаблица с помощью цикла:')
count = (finish - start) // n + 1
code = start
for i in range(count):
    row = ''
    for j in range(n):
        if code > finish:
            break

        row += f'{code:>3} - {chr(code):<4}'
        code += 1

    print(row)
