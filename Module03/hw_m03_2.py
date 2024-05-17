def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(a=12345, c=False)
print_params(b = 25)
print_params(c = [1,2,3])

print()

values_list = [1, 'dva', True]
values_dict = {'a': 'netu', 'b': 777, 'c': 'est!'}

print_params(*values_list)
print_params(**values_dict)

print()

values_list_2 = [21, 'loooooooooong']
print_params(*values_list_2, 42)   # it works

