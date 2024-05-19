def square_def(x):
    return x ** 2

def factorial_def(n):
    if n == 0:
        return 1
    else:
        return n * factorial_def(n - 1)

square_lambda = lambda x: x ** 2
print(square_lambda(7))
print(square_def(7))

factorial_lambda = (lambda f: (lambda x: f(f, x)))(lambda f, x: 1 if x == 0 else x * f(f, x - 1))
print(factorial_lambda(6))
print(factorial_def(6))

