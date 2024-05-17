class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        if isinstance(other, Building):
            return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
        else:
            return False

building1 = Building(10, "Residential")
building2 = Building(5, "Residential")
building3 = Building(10, "Residential")
building4 = Building(8, "Commercial")

print(building1 == building2)
print(building1 == building3)
print(building1 == building4)
