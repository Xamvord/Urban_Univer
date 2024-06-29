import pandas as pd

data = pd.read_csv('data.csv')
print("Данные из CSV файла:")
print(data)

print()
print('# ------------------------------------------------------------------------------------- #')

print("\nОписательная статистика:")
print(data.describe())

print("\nИнформация о данных:")
print(data.info())

print()
print('# ------------------------------------------------------------------------------------- #')

# Фильтрация данных (возраст больше 30)
filtered_data = data[data['age'] > 30]
print("\nСотрудники старше 30 лет:")
print(filtered_data)

# Добавление нового столбца с увеличенной зарплатой на 10%
data['salary_increased'] = data['salary'] * 1.1
print("\nДанные с увеличенной зарплатой:")
print(data)

print()
print('# ------------------------------------------------------------------------------------- #')

# Группировка данных по городу и вычисление средней зарплаты
grouped_data = data.groupby('city')['salary'].mean()
print("\nСредняя зарплата по городам:")
print(grouped_data)

print()
print('# ------------------------------------------------------------------------------------- #')

data.to_csv('processed_data.csv', index=False)
print("\nОбработанные данные сохранены в файл processed_data.csv")
