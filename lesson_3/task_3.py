"""3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

from random import randint

left, right = -100, 100
numbers = [randint(left, right) for i in range(30)]

min_num, max_num = right, left - 1
min_pos, max_pos = 0, 0

print(numbers)

# ищем первые вхождения минимального и максимального элементов
for i, num in enumerate(numbers):
    if num > max_num:
        max_num, max_pos = num, i
    elif num < min_num:
        min_num, min_pos = num, i

numbers[min_pos], numbers[max_pos] = numbers[max_pos], numbers[min_pos]

print(f"Минимальный: {min_num}, позиция: {min_pos}")
print(f"Максимальный: {max_num}, позиция: {max_pos}")
print(numbers)
