class THouse:
    numberOfFloors = 10


my_house = THouse()

for floor in range(1, my_house.numberOfFloors + 1):
    print(f"Текущий этаж равен {floor}.")
