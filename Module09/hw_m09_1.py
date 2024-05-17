nums = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

def pwr_2(x):
    return (x ** 2)

def is_odd(x):
    return x % 2

list_sqr = filter(is_odd, map(pwr_2, nums))

print('Input numbers:', nums)
print('Odd squares of input:', list(list_sqr))

