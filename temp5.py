#Задача 10

import random

number_coins = int(input())
coins_1 = 0
coins_0 = 0
for i in range(number_coins):
    side = random.randint(0, 1)
    print(f'сторона {i + 1} монетки{side}')
    if side == 1:
        coins_1 += 1
    else:
        coins_0 += 1
if coins_1 < coins_0:
    print(f'Мин. перевернуть{coins_1}')
else:
    print(f'Мин. перевернуть {coins_0}')