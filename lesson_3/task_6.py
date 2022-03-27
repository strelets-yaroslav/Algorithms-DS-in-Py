"""6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать."""

from random import randint

left, right = -100, 100
numbers = [randint(left, right) for i in range(30)]

min_num, max_num = right, left - 1
min_pos, max_pos = 0, 0

# находим первые вхождения мин и макс элементов
for i, num in enumerate(numbers):
    if num < min_num:
        min_num, min_pos = num, i
    elif num > max_num:
        max_num, max_pos = num, i

res = f"Сумма между {min_num} ({min_pos}) и {max_num} ({max_pos})"

if min_pos > max_pos:
    min_pos, max_pos = max_pos, min_pos

nums_sum = 0
if min_pos != max_pos:  # для проверки случая, когда в массиве одинаковые числа
    for i in range(min_pos + 1, max_pos):
        nums_sum += numbers[i]

print(numbers)
print(f"{res} равна {nums_sum}")
