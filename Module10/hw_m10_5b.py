import multiprocessing


def process_request(data, request):
    product, action, quantity = request
    if action == "receipt":
        if product in data:
            data[product] += quantity
        else:
            data[product] = quantity
    elif action == "shipment":
        if product in data and data[product] >= quantity:
            data[product] -= quantity
        else:
            print(f"Невозможно отгрузить {quantity} единиц {product}: недостаточно на складе")


class WarehouseManager:
    def __init__(self):
        self.manager = multiprocessing.Manager()
        self.data = self.manager.dict()

    def run(self, requests):
        processes = []
        for request in requests:
            p = multiprocessing.Process(target=process_request, args=(self.data, request))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()


if __name__ == "__main__":
    # Создаем менеджера склада
    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    # Запускаем обработку запросов
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print(dict(manager.data))
