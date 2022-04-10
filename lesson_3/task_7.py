"""7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться."""

from random import randint

left, right = -100, 100
numbers = [randint(left, right) for i in range(30)]

min_num, min_num2 = right, right

for num in numbers:
    if num <= min_num:
        min_num, min_num2 = num, min_num
    elif num < min_num2:
        min_num2 = num

print(numbers)
if min_num == min_num2:
    print(f"Оба минимальных элемента равны: {min_num}")
else:
    print(f"Минимальный элемент - {min_num}, второй минимальный - {min_num2}")
