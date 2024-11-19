immutable_var = ("самолет", 1, 3.6, False, [8, 9, 11])
print('Immutable tuple:',immutable_var)

# immutable_var[2] = 5.5
# print(immutable_var)

# Попытка изменить элемент кортежа приводит к ошибке "TypeError", потому что кортежи в Python являются неизменяемыми (immutable).
# Кортежи хранят ссылки на свои элементы, а не сами элементы, соответственно, когда мы пытаемся изменить элемент кортежа, мы на самом деле пытаемся изменить ссылку на элемент.
# Изменениям могут подвергаться только элементы списка, содержащегося в кортеже.

mutable_list = ["самолет", 1, 3.6, False]
print('Mutable list:',mutable_list)
mutable_list[0] = "поезд"
mutable_list[2] = 6.3
mutable_list[3] = "билет"
print('Mutable list(modified):',mutable_list)