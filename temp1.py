n = int(input("Введите число: "))

c = n % 10
n = n // 10
b = n % 10
a = n // 10

print(a + b + c)