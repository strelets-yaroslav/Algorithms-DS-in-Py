"""1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут."""


from random import randint
import operator


def bubble_sorting(arr, asc=False):
    """
    Сортировка пузырьком.

    :param arr: исходный массив чисел,
    :param asc: True - по возрастанию (default False).
    """
    compare = operator.gt if asc else operator.lt
    n, is_changed = len(arr) - 1, True
    counts, full_counts = 0, 0

    while is_changed:
        is_changed = False
        counts += 1
        full_counts += n
        for i in range(n):
            if compare(arr[i], arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_changed = True  # если нет обменов, сортировка завершена
                n = i  # запоминаем индекс последнего обмена - после него проверять уже не надо

    print(f'Число верхних проходов: {counts}, всех: {full_counts}')


numbers = [randint(-100, 99) for _ in range(20)]
print(f'Исходный: {numbers}')
bubble_sorting(numbers)
print(f'Отсортированный: {numbers}')
