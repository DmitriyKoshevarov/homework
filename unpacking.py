def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(2,False)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [5.2, 'string', False]
values_dict = {'a':True, 'b':112, 'c':'word'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['apple', 17]
print_params(*values_list_2, 42)