def generate_password(n):
    pairs = []
    password = ''
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                pairs.append((i, j))
    for pair in pairs:
        password += str(pair[0]) + str(pair[1])
    return password

n = int(input("Введите число от 3 до 20: "))
if n < 3 or n > 20:
    print("Число должно быть от 3 до 20!")
else:
    result = generate_password(n)
    print(f"Пароль для числа {n}: {result}")

