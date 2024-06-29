import numpy as np

# Создание массива из списка
array = np.array([1, 2, 3, 4, 5])
print("Массив:", array)

# Умножение всех элементов массива на 2
array_multiplied = array * 2
print("Умноженный на 2 массив:", array_multiplied)

# Сумма всех элементов массива
sum_of_elements = np.sum(array)
print("Сумма элементов массива:", sum_of_elements)

# Среднее значение элементов массива
mean_of_elements = np.mean(array)
print("Среднее значение элементов массива:", mean_of_elements)

print()
print('# ------------------------------------------------------------------------------------- #')

# Создание матрицы 3x3
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Матрица 3x3:")
print(matrix)

# Транспонирование матрицы
transposed_matrix = np.transpose(matrix)
print("Транспонированная матрица:")
print(transposed_matrix)

# Умножение двух матриц
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
multiplied_matrix = np.dot(matrix, matrix2)
print("Результат умножения матриц:")
print(multiplied_matrix)

print()
print('# ------------------------------------------------------------------------------------- #')

# Создание массива с линейным распределением от 0 до 10 с шагом 0.5
linear_array = np.arange(0, 10, 0.5)
print("Массив с линейным распределением:", linear_array)

# Применение синусоидальной функции к каждому элементу массива
sin_array = np.sin(linear_array)
print("Синусоида массива:")
print(sin_array)

# Создание массива случайных чисел
random_array = np.random.rand(5)
print("Массив случайных чисел:", random_array)

# Нахождение максимального и минимального значения в массиве случайных чисел
max_value = np.max(random_array)
min_value = np.min(random_array)
print("Максимальное значение в массиве случайных чисел:", max_value)
print("Минимальное значение в массиве случайных чисел:", min_value)
