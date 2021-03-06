"""1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака."""

# 5 = 00000101, 6 = 00000110

num_and = 5 & 6  # 00000100 = 4
num_or = 5 | 6  # 00000111 = 7
num_xor = 5 ^ 6  # 00000011 = 3

left_bit_shift = 5 << 2  # 00010100 = 20
right_bit_shift = 5 >> 2  # 00000001 = 1

print(f'Побитовое И: {num_and}')
print(f'Побитовое ИЛИ: {num_or}')
print(f'Побитовое искл.ИЛИ: {num_xor}')
print(f'Побитовый сдвиг влево на 2: {left_bit_shift}')
print(f'Побитовое сдвиг вправо на 2: {right_bit_shift}')
