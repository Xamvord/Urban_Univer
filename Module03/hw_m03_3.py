def test(*args, **params):
    for i in args:
        print(i)
    print()
    for i in params.items():
        print(i)

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


test(1, 2, 3, 'Vasya', ['item1', 'item2', 'item3'], a='nothing', b=11, c=False)

print()

n = 5
print(f'Факториал числа {n} равен {fact(n)}')