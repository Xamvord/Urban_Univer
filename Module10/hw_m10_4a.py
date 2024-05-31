import threading
import queue
import time
from colorama import Fore, Style, init
init(autoreset=True)

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False
        self.lock = threading.Lock()

class Customer(threading.Thread):
    def __init__(self, customer_id, cafe, table):
        super().__init__()
        self.customer_id = customer_id
        self.cafe = cafe
        self.table = table

    def run(self):
        print(Fore.YELLOW + f"Посетитель номер {self.customer_id} сел за стол {self.table.number}")
        time.sleep(5)
        print(Fore.GREEN + f"Посетитель номер {self.customer_id} покушал и ушёл.")
        self.cafe.release_table(self.table)

class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables
        self.tables_lock = threading.Lock()
        self.active_threads = []

    def customer_arrival(self):
        for customer_id in range(1, 21):
            print(f"Посетитель номер {customer_id} прибыл.")
            self.serve_customer(customer_id)
            time.sleep(1)

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
        next_customer_id = None
        with self.tables_lock:
            if not self.queue.empty():
                next_customer_id = self.queue.get()
                self.show_queue()
                table.is_busy = True
        if next_customer_id:
            customer = Customer(next_customer_id, self, table)
            self.active_threads.append(customer)
            customer.start()

# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()

# Ожидаем завершения всех активных потоков
for thread in cafe.active_threads:
    thread.join()
