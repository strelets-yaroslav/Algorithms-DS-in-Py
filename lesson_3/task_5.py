"""5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения."""

from random import randint

left, right = -100, 100
numbers = [randint(left, right) for i in range(30)]

max_neg, pos = left - 1, -1
for i, num in enumerate(numbers):
    if 0 > num > max_neg:
        max_neg, pos = num, i

print(numbers)
print(f"Максимальный отрицательный элемент {max_neg} на позиции {pos}")
