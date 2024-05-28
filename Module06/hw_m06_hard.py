import math

class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self.__color = list(color)
        self.filled = False
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

# =========================================
class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        return self.get_sides()[0] / (2 * math.pi)

    def get_area(self):
        return math.pi * (self.__radius ** 2)

# =========================================
class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        self.__height = self.__calculate_height()

    def __calculate_height(self):
        height = 2 * self.get_area() / self.get_sides()[0]
        return height

    def get_area(self):
        a, b, c = self.get_sides()
        p_half = sum(self.get_sides()) / 2
        area = math.sqrt(p_half * (p_half - a) * (p_half - b) * (p_half - c))
        return area

# =========================================
class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), *sides):
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
        elif len(sides) != self.sides_count:
            sides = [1] * self.sides_count
        super().__init__(color, *sides)

    def set_sides(self, *sides):
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
        super().set_sides(*sides)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3

# =========================================
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
