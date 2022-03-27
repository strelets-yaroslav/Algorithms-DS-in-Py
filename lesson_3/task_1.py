"""1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов."""

digits = range(2, 10)
counts = dict.fromkeys(digits, 0)
for num in range(2, 100):
    for i in digits:
        if num % i == 0:
            counts[i] += 1

print(counts)
