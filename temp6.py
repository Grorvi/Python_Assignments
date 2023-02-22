#Задача 12:

import math
sum = int(input())
prod = int(input())
x = (sum + math.sqrt(sum ** 2 - 4 * prod)) / 2
if x % 1 != 0:
    print('ошибка ввода')
else:
    print(f'X = {round(x)}, Y = {sum - round(x)}')