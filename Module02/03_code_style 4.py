# -*- coding: utf-8 -*-

# блоки кода

num_x, num_y = 10, 29

if num_x < 0:
    print('Х меньше нуля')
    num_z = num_x ** 2 + num_y
else:
    print('Х больше нуля')
    num_z = num_x - num_y
print('Результат:', num_z)

# ср. с С++

# if (x < 0) { printf('Меньше нуля\n'); z = x**2 + y; } else { printf('Больше нуля\n'); z = x - y; } printf('Получается\n', z)

# вложенные блоки кода

name = input('Enter your name >>> ')
if name == 'Ola':
    opponent = 'Ola'
    print('Hi, Ola!')
else:
    if name == 'Sofi':
        opponent = 'Sofi'
        print('Hi, Sofi!')
    else:
        if name == 'Katy':
            opponent = 'Katy'
            print('Hi, Katy!')
        else:
            opponent = 'anonymous'
            print('Hi, anonymous!')

# оператор pass

if num_x < 0:
    if num_y > 0:
        num_z = -num_x + num_y
    else:
        num_z = -num_x - num_y
else:
    num_z = num_x + num_y

# соглашения о стиле кода
# PEP8 (Python Enhancement Proposal 8) - описан "правильный" стиль программирования в пайтон
# https://www.python.org/dev/peps/pep-0008/

# 4 пробела на каждый уровень отступа

if num_x < 0:
    if num_y > 0:
        pass
    else:
        print('направо!')
else:
    print('стой!')

# Максимальная длина строки

my_poem = ['Варкалось, хливкие шорьки пырялись по наве', 'И хрюкотали зелюки как мюмзики в мове',
           'О бойся Бармаглота, сын! Он так свирлеп и дик', 'А в глуше рымит исполин - Злопастный Брандашмыг!']

# пробелы в операторах

x = 2
y = x * x + 1
is_big = x >= 3000

line_of_poem = my_poem[-1]
print(line_of_poem)
my_numbers_list = [2, 3, 4, 5, 6]

# reformat кода

just_x, just_y = 3, 8

if just_x == 3:
    print(42)

if just_x < 0:
    if just_y > 0:
        print('налево!')
    else:
        print('направо!')
else:
    print('стой!')


# названия переменных

count_of_my_pets = 34
if count_of_my_pets > 10:
    print('I need more space for my pets!')

my_favorite_pets_and_bird = ['cat', 'wolf', 'ostrich']
if 'lion' in my_favorite_pets_and_bird:
    print('Wow!')

#MyFavoritePetsAndBirds = ['cat', 'wolf', 'ostrich']
# но такой стиль используется для названий классов
my_favorite_pets_and_birds_2 = ['cat', 'hedgehog', 'ostrich', 'shooshpanchik']


# рекомендации PEP8

# b (одиночная маленькая буква)
# B (одиночная заглавная буква)
# но лучше использовать только такие однобуквенные имена
#   i j k - для циклов
#   x y z - для координат

# никогда не используйте в названиях переменных одиночные l, I, O  !
num_length = 34
num_width = 43
if num_length > num_width:
    print('length is greater than width')

num_oops = 9
if num_oops > 0:
    print('num_oops is greater than zero')

# lowercase (слово в нижнем регистре)
# lower_case_with_underscores (слова из маленьких букв с подчеркиваниями)
# UPPERCASE (заглавные буквы)
# UPPERCASE_WITH_UNDERSCORES (слова из заглавных букв с подчеркиваниями)

# CapitalizedWords (слова с заглавными буквами, или CapWords, или CamelCase).
#   Замечание: когда вы используете аббревиатуры в таком стиле, пишите все буквы аббревиатуры заглавными —
#   HTTPServerError лучше, чем HttpServerError.

# mixedCase (отличается от CapitalizedWords тем, что первое слово начинается с маленькой буквы)
# Capitalized_Words_With_Underscores (слова с заглавными буквами и подчеркиваниями — уродливо!)


# автоматическое переименование в PyCharm и подсказки - вам не нужно набирать длинные названия переменных

animals_list = ['cat', 'wolf', 'ostrich', 'lion']
if 'lion' in animals_list:
    print('Wow!')

# В каждой уважающей себя компании есть style guide (стайл-гайд) - руководство по стилю написания кода.
# Практически все они основываются на PEP8, с небольшими исключениями, принятыми в этой команде.
# Как пример стайл-гайда небольшой компании рекомендую почитать
# https://github.com/best-doctor/guides/blob/master/guides/python_styleguide.md
