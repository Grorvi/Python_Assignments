#Задача 14:

num = int(input())
prod = 0
degree = 0
while prod * 2 < num:
    prod = 2 ** degree
    print(prod, end= ' ')
    degree += 1