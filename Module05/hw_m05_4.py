class TBuilding:
    total = 0

    def __init__(self):
        TBuilding.total += 1

buildings = [TBuilding() for _ in range(40)]

print(f"Total number of Building instances: {TBuilding.total}")
