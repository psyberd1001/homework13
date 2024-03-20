# *args - списки кортежи и прочее, **rwargs - словари т.е. ключ + значение

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a = 2)
print_params(b = 3, c = 'тоже строка')
print_params(b = 25, c = [1, 2, 3])
print_params(a = 24, b = 'Ramos', c = [1, 2, 3])


values_list = [5, 'Dementor', True]
values_dict = {'a': 4, 'b': 'Alahamora', 'c': False}
values_list_2 = [92 , 'Аммитабха']

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
