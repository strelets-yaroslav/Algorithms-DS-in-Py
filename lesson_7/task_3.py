"""3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
(сортировка слиянием также недопустима)."""


from random import randint, choice


def find_median(arr, m):
    """
    Рекурсивный поиск медианы.

    :param arr: массив чисел,
    :param m: индекс медианы,
    :return: значение медианы.
    """
    if len(arr) == 1:
        assert m == 0  # проверка корректности массива
        return arr[0]  # медиана найдена (прошли до самого конца)

    pivot = choice(arr)  # выбираем опорный элемент

    left = [num for num in arr if num < pivot]
    right = [num for num in arr if num > pivot]
    pivots = [num for num in arr if num == pivot]

    len_left, len_middle = len(left), len(left) + len(pivots)

    if m < len_left:  # медиана в массиве меньших элементов
        return find_median(left, m)
    elif m < len_middle:  # медиана найдена (выход раньше)
        return pivot
    else:  # медиана в массиве бОльших элементов
        return find_median(right, m - len_middle)


m = 10
numbers = [randint(0, 100) for _ in range(2 * m + 1)]
print(f'Исходный массив: {numbers}')
print(f'Медиана с помощью алгоритма quickselect Хоара = {find_median(numbers, m)}')
print('Проверка: ' + '*' * 100)
s_numbers = sorted(numbers)
print(f'Отсортированный массив: {s_numbers}')
print(f'Медиана по индексу {m} = {s_numbers[m]}')
