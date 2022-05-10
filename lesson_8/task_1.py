"""1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа."""


def handshakes(n):
    if n < 2:
        return "Задано некорректное число друзей."

    g = [(i, j) for i in range(n - 1) for j in range(i + 1, n)]
    return len(g), g


friends_count = int(input('Введите количество друзей: '))
res, friends = handshakes(friends_count)
print(f'Число рукопожатий: {res}')
print(f'Другой способ - сумма арифм.прогрессии по n-1 членам: {int(friends_count * (friends_count - 1) / 2)}')
print('Граф рукопожатий в виде списка рёбер:')
print(*friends, sep='\n')
