"""1. Проанализировать скорость и сложность одного любого алгоритма из разработанных
 рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом
   (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему."""

import cProfile

# Для анализа была взята задача №4 из 2-го урока: найти сумму n элементов ряда чисел: 1, -0.5, 0.25, -0.125,…


def sum_1(n):
    """Нахождение суммы с помощью формулы для n-го члена ряда - в лоб."""
    s = 0
    for i in range(n):
        s += (-1) ** i * 2 ** (-i)
    return s


# sum_1(10)     1000 loops, best of 5: 8.29 usec per loop
# sum_1(100)    1000 loops, best of 5: 87.4 usec per loop
# sum_1(200)    1000 loops, best of 5: 269 usec per loop
# sum_1(500)    1000 loops, best of 5: 690 usec per loop
# sum_1(1000)   1000 loops, best of 5: 1.38 msec per loop
# sum_1(10000)  1000 loops, best of 5: 14 msec per loop

# cProfile.run('sum_1(10000)')
# 4 function calls in 0.020 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.014    0.014 <string>:1(<module>)
#         1    0.014    0.014    0.014    0.014 task_1.py:14(sum_1)
#         1    0.006    0.006    0.020    0.020 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод: довольно медленный способ.

def sum_2(n):
    """Оптимизация вычислений через предыдущий член ряда."""
    s = 0
    item = 1
    for i in range(n):
        s += item
        item *= -.5
    return s


# sum_1(10)     1000 loops, best of 5: 2.9 usec per loop
# sum_1(100)    1000 loops, best of 5: 13.6 usec per loop
# sum_1(200)    1000 loops, best of 5: 40.6 usec per loop
# sum_1(500)    1000 loops, best of 5: 107 usec per loop
# sum_1(1000)   1000 loops, best of 5: 210 usec per loop
# sum_1(10000)  1000 loops, best of 5: 1.55 msec per loop

# cProfile.run('sum_2(10000)')
# 4 function calls in 0.003 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.003    0.003    0.003    0.003 task_1.py:32(sum_2)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод: быстрый способ, как и первый не занимает много памяти.


def sum_3(n):
    """Попытка использовать 'красоту' оформления кода - должен быть медленнее."""
    row = [1.]
    [row.append(-.5 * row[-1]) for i in range(n-1)]

    return sum(row)


# sum_1(10)     1000 loops, best of 5: 2.71 usec per loop
# sum_1(100)    1000 loops, best of 5: 19.5 usec per loop
# sum_1(200)    1000 loops, best of 5: 59.4 usec per loop
# sum_1(500)    1000 loops, best of 5: 170 usec per loop
# sum_1(1000)   1000 loops, best of 5: 306 usec per loop
# sum_1(10000)  1000 loops, best of 5: 2.93 msec per loop

# cProfile.run('sum_3(10000)')
# 10005 function calls in 0.009 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.009    0.009 <string>:1(<module>)
#         1    0.000    0.000    0.008    0.008 task_1.py:52(sum_3)
#         1    0.006    0.006    0.008    0.008 task_1.py:55(<listcomp>)
#         1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#      9999    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод: так же быстрее первого, но уступает второму и по производительности, и по использованию памяти.

# Общий вывод: второй способ наиболее оптимальный по производительности и по использованию памяти,
# т.к. реализует оптимизированные вычисления за один проход без использования встроенных методов.
