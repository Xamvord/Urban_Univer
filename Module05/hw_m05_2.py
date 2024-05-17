class THouse:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f"Количество этажей в моем доме установлено в {self.numberOfFloors}.")

my_house = THouse()

my_house.setNewNumberOfFloors(5)
