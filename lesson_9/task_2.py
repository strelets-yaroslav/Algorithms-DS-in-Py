"""Закодируйте любую строку по алгоритму Хаффмана."""

import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    """
    Класс для хранения структуры дерева в виде узлов с ветвями
    """
    def go(self, codes, enc):
        """
        Метод обхода дерева по узлам.

        :param codes: таблица кодирования в виде словаря
        :param enc: кодированное представление текущего символа
        :return: возвращаемого значения нет - меняется сама таблица кодирования при обходе дерева
        """
        self.left.go(codes, enc + "0")  # для левого потомка добавляем 0
        self.right.go(codes, enc + "1")  # для правого - 1


class Leaf(namedtuple("Leaf", ["symbol"])):
    """
    Класс для хранения информации о значении символа (конечные элементы дерева)
    """
    def go(self, codes, enc):
        """
        Метод завершения обхода дерева по определённому пути.

        :param codes: таблица кодирования в виде словаря
        :param enc: кодированное значение текущего символа
        :return: возвращаемого значения нет - меняется сама таблица кодирования при обходе дерева
        """
        codes[self.symbol] = enc


class Huffman:
    """
    Класс кодирования/декодирования по алгоритму Хаффмана.
    Хранятся две таблицы: кодирования и декодирования
    (вторая получается переворачиванием пар ключ-значение из первой)
    """
    __enc_codes = None  # таблица кодирования
    __dec_codes = None  # таблица декодирования (для простоты обработки)

    def __init__(self):
        self.__enc_codes = {}
        self.__dec_codes = {}

    def get_codes(self, enc=True):
        """
        Получение элементов таблицы кодирования/декодирования.

        :param enc: True (default) - кодирования, иначе - декодирования
        :return: элементы таблицы кодирования/декодирования
        """
        if enc:
            return self.__enc_codes.items()
        else:
            return self.__dec_codes.items()

    def encode(self, s):
        """
        Метод кодирования по алгоритму Хаффмана.

        :param s: исходная строка
        :return: кодированная строка
        """
        assert len(s) > 1, 'Нечего кодировать!'

        heap = []  # очередь с приоритетами
        # очередь строится с помощью счётчика, уникального для всех листьев
        for char, freq in Counter(s).items():
            # храним в очереди частоту символа, счётчик и сам символ
            heap.append((freq, len(heap), Leaf(char)))

        heapq.heapify(heap)  # формируем очередь с приоритетами (мин.куча)
        count = len(heap)
        while len(heap) > 1:  # пока в очереди есть минимум два элемента
            # забираем из очереди левый и правый элементы с минимальными частотами
            freq_left, _, left = heapq.heappop(heap)
            freq_right, _, right = heapq.heappop(heap)
            # добавляем узел для этих элементов с их суммарной частотой в дерево обхода
            heapq.heappush(heap, (freq_left + freq_right, count, Node(left, right)))
            count += 1

        if heap:  # начальная строка не была пустой/одним символом
            [(_, _, root)] = heap  # в очереди остался один элемент - корень дерева
            root.go(self.__enc_codes, "")  # обходим дерево, строя таблицу кодирования

        # формируем таблицу декодирования
        self.__dec_codes = {v: k for k, v in self.__enc_codes.items()}

        # получаем кодированную строку
        enc_str = "".join(self.__enc_codes[char] for char in s)

        # проверка на пустую кодированную строку
        return enc_str or "Что-то пошло не так - кодирование не удалось."

    def decode(self, enc_str):
        """
        Метод декодирования по алгоритму Хаффмана.

        :param enc_str: кодированная строка
        :return: декодированная строка
        """
        dec_str, enc_code = "", ""
        for char in enc_str:  # обходим кодированную строку посимвольно
            enc_code += char  # формируем код
            if enc_code in self.__dec_codes:  # если код найден - декодируем
                dec_str += self.__dec_codes[enc_code]
                enc_code = ""

        # грубая проверка соответствия кодированной строки таблице кодирования - если dec_str пустая
        return dec_str or "Строка не соответствует таблице кодирования."


user_string = input("Введите строку для кодирования: ")
huffman = Huffman()
encoded = huffman.encode(user_string)
print("Строка в закодированном виде:")
print(encoded)
print("Таблица кодирования:")
for k, v in huffman.get_codes():
    print(f"{k} -> {v}")
print("Декодированная строка:")
print(huffman.decode(encoded))
