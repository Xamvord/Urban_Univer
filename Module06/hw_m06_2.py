class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"


class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return "Количество лошадиных сил неизвестно"

class Nissan(Vehicle, Car):
    def __init__(self):
        Vehicle.__init__(self)
        Car.__init__(self)
        self.vehicle_type = "car"
        self.price = 1700000

    def horse_powers(self):
        return 231

nissan = Nissan()

print(f"Тип транспортного средства: {nissan.vehicle_type}")
print(f"Цена: {nissan.price} рублей")
print(f"Лошадиные силы: {nissan.horse_powers()}")
