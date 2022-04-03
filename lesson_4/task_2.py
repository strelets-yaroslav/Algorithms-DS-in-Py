"""2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать
соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена»."""


from math import log, sqrt


def sieve(k):
    """Решето Эратосфена."""
    n = int(1.5 * k * log(k)) + 1  # верхняя оценка для простого числа

    if n < 2:
        return n

    num_list = [i for i in range(n)]
    s_count, s_num, i = 0, 0, 2
    while s_count < k:
        if num_list[i] != 0:
            s_num = num_list[i]
            s_count += 1
            for j in range(i, n, i):
                num_list[j] = 0
        i += 1

    return s_num


# sieve(10)         100 loops, best of 5: 22.1 usec per loop
# sieve(50)         100 loops, best of 5: 163 usec per loop
# sieve(100)        100 loops, best of 5: 418 usec per loop
# sieve(1000)       100 loops, best of 5: 7.05 msec per loop
# sieve(10000)      100 loops, best of 5: 109 msec per loop

# Сложность решета: О(n * log(log(n))) - внешний цикл - n, внутренний - log(log(n))


def simple_num(k):
    """Поиск простых чисел: используется проход только по нечётным, а также
       исключаются кратные 5 (большие 10). Также не используем память для исходных чисел."""
    s_num_list = [2]
    s_count, num = 1, 3
    while s_count < k:
        if (num > 10) and (num % 10 == 5):
            num += 2
            continue
        for s_num in s_num_list:
            if s_num * s_num - 1 > num:  # проверять нужно только числа, меньшие корня из текущего.
                s_num_list.append(num)
                s_count += 1
                break
            if num % s_num == 0:  # число кратно текущему простому.
                break
        else:  # в цикле не сработало ни одно условие прерывания - значит, простое.
            s_num_list.append(num)
            s_count += 1
        num += 2

    return s_num_list[-1]


# simple_num(10)            100 loops, best of 5: 15.5 usec per loop
# simple_num(50)            100 loops, best of 5: 131 usec per loop
# simple_num(100)           100 loops, best of 5: 360 usec per loop
# simple_num(1000)          100 loops, best of 5: 9.1 msec per loop
# simple_num(10000)         100 loops, best of 5: 254 msec per loop

# На небольших значениях данный алгортим лучше решета,
# но с ростом размерности он начинает теряет в производительности
# из-за увеличения времени прохода по массиву простых чисел.
# Сложность можно оценить, как О(n * n / log(n)):
# внешний цикл, как и в решете - n, внутренний - k = n / log(n) (кол-во простых чисел для n)


def sieve_2(k):
    """Оптимизированное решето - используется массив флагов для чисел."""
    n = int(1.5 * k * log(k)) + 1

    if n < 2:
        return n

    flags = [1] * n  # флаги для чисел, 0-й относится к простому числу 2
    sqrt_n = int(sqrt(n)) + 1  # проверять можно только числа, меньшие корня из верхней границы
    for i in range(2, sqrt_n):
        if flags[i - 2]:  # если флаг взведён, то на данной итерации это простое число.
            for j in range(i + i, n + 1, i):  # обнуляем флаги для всех чисел, кратных ему.
                flags[j - 2] = 0

    # к-е простое число находим как индекс к-го взведённого флага в получившемся массиве.
    i = 0
    while k:
        k -= flags[i]
        i += 1

    return i + 1


# sieve_2(10)           100 loops, best of 5: 14.7 usec per loop
# sieve_2(50)           100 loops, best of 5: 105 usec per loop
# sieve_2(100)          100 loops, best of 5: 272 usec per loop
# sieve_2(1000)         100 loops, best of 5: 4.88 msec per loop
# sieve_2(10000)        100 loops, best of 5: 74.5 msec per loop

# Производительность алгоритма лучше обычной реализации решета из-за
# отсутствия вычислительных операций и уменьшения внешнего цикла.
# Сложность: О(sqrt(n) * log(log(n))) + O(k * log(k))
# внешний цикл - sqrt(n), внутренний - log(log(n))
# + цикл по флагам = k * log(k)


# n = 1000
# print(sieve(n))
# print(sieve_2(n))
# print(simple_num(n))
