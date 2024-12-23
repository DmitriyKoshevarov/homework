# Задача на For:
# 1.
# На вход программе подается натуральное число 𝑛. Напишите программу, которая выводит звездный треугольник в соответствии с примером.
#
# n = 3
#
# *
# **
# ***

n=3

for factor in range(1,n+1):
    triangle = '*' * factor
    print(triangle)

print()

# 2.
# Напишите программу, на вход которой даются четыре числа a, b, c и d
# Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [𝑎;𝑏] на все числа отрезка [𝑐;𝑑].
# Числа 𝑎, b, c и 𝑑 являются натуральными и не превосходят 10, 𝑎≤𝑏, 𝑐≤𝑑.
# Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции. Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы.
#
# a,b,c,d = 7,10,5,6
#
#     5     6
# 7  35  42
# 8  40  48
# 9  45  54
# 10  50  60


a,b,c,d = 7,10,5,6
print('\t', end='')
for i in range(c,d+1):
    print(i, end='\t')
print()
for i in range(a,b+1):
    print(i, end='\t')
    for j in range(c,d+1):
        print(i*j,end='\t')
    print()

# Дано натуральное число 𝑛. Напишите программу, которая печатает численный треугольник с высотой равной n, в соответствии с примером:
#
# n =  6
#
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
#
# ___________________________
# Данные, которые будут подаваться на вход ——> ф-ия input()

print()

i = 1
n = int(input('Введите высоту треугольника: '))
for string_number in range(1, n+1):
    for numbers in range(string_number):
        print(i, end = ' ')
        i += 1
    print()