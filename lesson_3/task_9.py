"""9. Найти максимальный элемент среди минимальных элементов столбцов матрицы."""

from random import randint

left, right = 0, 10
rows, cols = 5, 7
matrix = [[randint(left, right) for _ in range(cols)] for _ in range(rows)]

mins = [right for _ in range(cols)]
max_min, pos = left - 1, 0

print("Матрица:")
for i in range(rows):
    for j, num in enumerate(matrix[i]):
        print(f"{matrix[i][j]:>5}", end='')
        if num < mins[j]:
            mins[j] = num
    print()

# ищем первый столбец с макс значением
for i, num in enumerate(mins):
    if max_min < num:
        max_min, pos = num, i

print("Минимальные значения по столбцам:")
print(mins)
print(f"Первый максимальный из них - {pos}-й столбец со значением {max_min}")
