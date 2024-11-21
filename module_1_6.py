my_dict = {'Vanya': 1990, 'Petya': 1995,'Roma': 2002}
print('Dict:',my_dict)
print('Existing value:',my_dict['Petya'])
print('Not existing value:',my_dict.get('Sasha'))
my_dict.update({'Masha': 1999, 'Sveta': 2004})
x = my_dict.pop('Roma')
print('Deleted value:',x)
print('Modified dictionary:',my_dict)

print()

my_set = {4,'Car', 4, 4, False, 2, 8, 'Train', 8.4, 'Car', 2, False}
print('Set:',my_set)
my_set.update({125, 'Bus'})
my_set.discard(False)
print('Modified set:',my_set)