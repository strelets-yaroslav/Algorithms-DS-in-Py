"""2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы."""


from random import random
import operator


def merge_sorting(arr, asc=True):
    """
    Сортировка слиянием.

    :param arr: исходный массив чисел,
    :param asc: True - по возрастанию (default True).
    :return: отсортированный массив чисел."""

    def merge_arr(l, r, asc):
        compare = operator.lt if asc else operator.gt  # по возрастанию - значит должно быть l < r
        res = []
        i, j = 0, 0
        len_l, len_r = len(l), len(r)
        while i < len_l and j < len_r:
            if compare(l[i], r[j]):
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1

        if i < len_l:
            res.extend(l[i:])

        if j < len_r:
            res.extend(r[j:])

        return res

    if len(arr) == 1:
        return arr[:]
    else:
        n = len(arr) // 2
        left = merge_sorting(arr[:n], asc)
        right = merge_sorting(arr[n:], asc)
        return merge_arr(left, right, asc)


numbers = [random() * 50 for _ in range(20)]
str_format = len(numbers) * '{:.2f} '
print(f'Исходный: [{str_format.format(*numbers)[:-1]}]')
print(f'Отсортированный: [{str_format.format(*merge_sorting(numbers))[:-1]}]')
