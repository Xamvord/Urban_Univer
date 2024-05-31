import threading
import queue
import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False
        self.lock = threading.Lock()

class Customer(threading.Thread):
    def __init__(self, customer_id, restaurant, table):
        super().__init__()
        self.customer_id = customer_id
        self.restaurant = restaurant
        self.table = table

    def run(self):
        print(Fore.YELLOW + f"Посетитель номер {self.customer_id} начал вкушать яства.")
        time.sleep(random.randint(3, 7))
        print(Fore.GREEN + f"Посетитель номер {self.customer_id} завершил трапезу и покинул ресторан.")
        self.restaurant.release_table(self.table)

class Restaurant:
    def __init__(self, n_tables):
        self.queue = queue.Queue()
        self.tables = [Table(i) for i in range(1, n_tables + 1)]
        self.tables_lock = threading.Lock()
        self.active_threads = []

    def customer_arrival(self):
        for customer_id in range(1, N_customers + 1):
            print(f"Посетитель номер {customer_id} прибыл.")
            # self.serve_customer(customer_id)
            self.queue.put(customer_id)
            self.show_queue()
            #time.sleep(0.5)
            time.sleep(random.uniform(0.3, 0.7))

    def serve_customer(self, customer_id):
        with self.tables_lock:
            table = None
            for t in self.tables:
                if not t.is_busy:
                    table = t
                    table.is_busy = True
                    break
        if table:
            customer = Customer(customer_id, self, table)
            self.active_threads.append(customer)
            customer.start()
        else:
            print(Fore.RED + f"Посетитель номер {customer_id} ожидает свободный стол.")
            self.queue.put(customer_id)
            self.show_queue()

    def show_queue(self):
        queue_list = list(self.queue.queue)
        if queue_list:
            print(Fore.BLUE + f"Текущая очередь: {', '.join(map(str, queue_list))}")
        else:
            print(Fore.CYAN + "Очередь пуста.")

    def release_table(self, table):
        with self.tables_lock:
            table.is_busy = False

    def headwaiter(self):
        while True:
            with self.tables_lock:
                for table in self.tables:
                    if not table.is_busy and not self.queue.empty():
                        next_customer_id = self.queue.get()
                        print(Fore.YELLOW + f"Метрдотель направляет посетителя номер {next_customer_id} за стол {table.number}.")
                        table.is_busy = True
                        customer = Customer(next_customer_id, self, table)
                        self.active_threads.append(customer)
                        customer.start()
                        self.show_queue()
            time.sleep(0.1)

# Количество столиков в ресторане
N_tables = 8

# Количество посетителей
N_customers = 50

# Инициализируем ресторан
restaurant = Restaurant(N_tables)

# Запускаем поток для метрдотеля
headwaiter_thread = threading.Thread(target=restaurant.headwaiter, daemon=True)
headwaiter_thread.start()

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=restaurant.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()

# Ожидаем завершения всех активных потоков
for thread in restaurant.active_threads:
    thread.join()
