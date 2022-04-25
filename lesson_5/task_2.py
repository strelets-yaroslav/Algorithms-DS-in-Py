"""2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа."""

from collections import deque, OrderedDict


class HexException(BaseException):
    def __init__(self, num_str):
        self.hex_num = num_str

    def __str__(self):
        return f'Недопустимое значение: {self.hex_num}'


class Hex:
    __map2hex = deque('0123456789ABCDEF')
    __rank = 16

    def __init__(self, num_iter):
        self.__map2dec = OrderedDict({self.__map2hex[i]: i for i in range(self.__rank)})
        self.hex_num = deque()
        try:
            for num in num_iter:
                if num.upper() not in self.__map2hex:
                    raise HexException(num)
                self.hex_num.append(num.upper())
        except TypeError:
            print('Не удалось создать экземпляр для Hex: был передан неитерируемый аргумент!')
            raise SystemExit

    def __str__(self):
        return ''.join(self.hex_num)

    def __add__(self, other):
        try:
            (a, b) = (self.hex_num.copy(), other.hex_num.copy()) if len(self.hex_num) > len(other.hex_num) \
                        else (other.hex_num.copy(), self.hex_num.copy())
        except AttributeError:
            print(f'Аргументы должны быть {self.__rank}-ными числами!')
            raise SystemExit

        add_res = deque()
        transfer, max_len = 0, len(a)
        for i in range(max_len):
            digit_1 = self.__map2dec[a.pop()]
            digit_2 = self.__map2dec[b.pop()] if len(b) > 0 else 0
            spam = digit_1 + digit_2 + transfer
            transfer = 1 if spam >= self.__rank else 0
            add_res.appendleft(self.__map2hex[spam % self.__rank])

        if transfer != 0:
            add_res.appendleft(self.__map2hex[transfer])

        return Hex(add_res)

    __iadd__ = __add__

    def __mul__(self, other):
        try:
            a, b = self.hex_num.copy(), other.hex_num.copy()
        except AttributeError:
            print('Аргументы должны быть 16-ными числами!')
            raise SystemExit

        mul_res = Hex('0')
        transfer, len_a, len_b = 0, len(a), len(b)
        for i in range(len_a):
            sub_res = deque()
            digit_1 = self.__map2dec[a.pop()]
            transfer = 0
            for j in range(len_b - 1, -1, -1):
                spam = digit_1 * self.__map2dec[b[j]] + transfer
                transfer = spam // self.__rank
                sub_res.appendleft(self.__map2hex[spam % self.__rank])

            if transfer != 0:
                sub_res.appendleft(self.__map2hex[transfer])

            [sub_res.append('0') for _ in range(i)]
            mul_res += Hex(sub_res)

        return mul_res

    __imul__ = __mul__


def sum_dec(a, b, r=16):
    return hex(int(a, r) + int(b, r)).upper()[2:]


def mul_dec(a, b, r=16):
    return hex(int(a, r) * int(b, r)).upper()[2:]


shex_1, shex_2 = 'a2', 'C4f'
hex_1, hex_2 = Hex(shex_1), Hex(shex_2)
print(f'{hex_1} + {hex_2} = {hex_1 + hex_2}')
print(f'Проверка: {sum_dec(shex_1, shex_2)}')
print(f'{hex_1} * {hex_2} = {hex_1 * hex_2}')
print(f'Проверка: {mul_dec(shex_1, shex_2)}')

while True:
    try:
        shex_3, shex_4 = input('Введите два шестнадцатиричных числа через пробел: ').split()
        hex_3, hex_4 = Hex(shex_3), Hex(shex_4)
        break
    except ValueError:
        print('Некорректные значения! Попробуйте снова.')
    except HexException as e:
        print(e)

print(f'{hex_3} + {hex_4} = {hex_3 + hex_4}')
print(f'Проверка: {sum_dec(shex_3, shex_4)}')
print(f'{hex_3} * {hex_4} = {hex_3 * hex_4}')
print(f'Проверка: {mul_dec(shex_3, shex_4)}')
