class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

rect = Rect(6, 7)
print(f"Стороны: {rect.a}, {rect.b}")
print(f"Площадь: {rect()}")
