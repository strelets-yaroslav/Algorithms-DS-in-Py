"""3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин."""

from random import randrange


def gen_graph(v):
    """
    Генерация графа из v вершин.

    :param v: число вершин
    :return: список смежностей
    """
    assert v > 1, 'Граф должен состоять из нескольких вершин.'

    g = {}
    for i in range(v):
        g[i] = set()
        edges = randrange(1, v)  # кол-во связанных вершин (минимум с одной)
        while len(g[i]) < edges:
            e = randrange(0, v)  # индекс вершины для связки
            if e != i:  # граф должен быть без петель
                g[i].add(e)

    return g


def dfs(g, s=0):
    """
    Обход графа в глубину.

    :param g: граф в виде списка смежностей
    :param s: вершина, с которой начинается обход
    :return: список родителей для каждой вершины, список пройденных вершин
    """
    length = len(g)
    is_visited = [False] * length
    parents = [None] * length
    way = []

    def _dfs_recursive(v):
        is_visited[v] = True
        way.append(v)

        for i in g[v]:
            if not is_visited[i]:
                parents[i] = v
                _dfs_recursive(i)  # идём вглубь к следующей связанной вершине
        else:
            way.append('<-' + str(v))  # возврат на пред. вершину

    _dfs_recursive(s)

    return parents, way


vertex_count = int(input("Число вершин: "))
graph = gen_graph(vertex_count)
print('Граф:')
for v, e in graph.items():
    print(f'Рёбра вершины {v}: {e}')

while True:
    start = input("С какой вершины производим обход ('q' для выхода): ")
    if start == 'q':
        break
    if not start.isdigit() or int(start) >= vertex_count:
        print("Введите корректное значение для вершины или 'q' для выхода.")
        continue

    parents, path = dfs(graph, int(start))
    print(f'Список родителей: {parents}')

    print('Путь обхода графа:')
    for i, v in enumerate(path):
        if i % 25 == 0:
            print()
        print(f'{v:>5};', end='')
    print()
