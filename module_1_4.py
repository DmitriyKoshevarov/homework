my_string = input('Введите текст: ')
#количество символов с учетом пробелов
print(len(my_string))
#количество символов без учета пробелов
print(len(my_string.replace(' ','')))
#вывод строки в верхнем регистре
print(my_string.upper())
#вывод строки в нижнем регистре
print(my_string.lower())
#вывод строки без пробелов
print(my_string.replace(' ',''))
#вывод первого символа строки
print(my_string[0])
#вывод последнего символа строки
print(my_string[-1])