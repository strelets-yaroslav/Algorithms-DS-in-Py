"""4. Определить, какое число в массиве встречается чаще всего."""

from random import randint

numbers = [randint(-10, 10) for i in range(30)]
counts = dict.fromkeys(frozenset(numbers), 0)

for num in numbers:
    counts[num] += 1

# ищем первое часто повторяющееся число
max_num, max_count = 0, 0
for num, count in counts.items():
    if count > max_count:
        max_num, max_count = num, count

print(numbers)
postfix = 'а' if (max_count % 10 in (2, 3, 4) and (max_count < 10 or max_count > 20)) else ''
print(f"Число {max_num} встречается {max_count} раз{postfix}.")
print(counts)

# выводим все числа, которые встречаются максимальное количество раз, если такие есть
often_nums = dict(filter(lambda item: item[1] == max_count, counts.items()))
if len(often_nums.keys()) > 1:
    print(f"Часто встречающиеся числа: {often_nums}")
