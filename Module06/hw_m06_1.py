class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return "Количество лошадиных сил неизвестно"


class Nissan(Car):
    def __init__(self):
        self.price = 1650000

    def horse_powers(self):
        return 231


class Kia(Car):
    def __init__(self):
        self.price = 2300000

    def horse_powers(self):
        return 250

nissan = Nissan()
kia = Kia()

print(f"Цена Nissan: {nissan.price} рублей; мощность двигателя, л.с.: {nissan.horse_powers()}")
print(f"Цена Kia: {kia.price} рублей; мощность двигателя, л.с.: {kia.horse_powers()}")
