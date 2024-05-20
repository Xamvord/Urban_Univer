import threading
import time

def print_numbers():
    for i in range(1, 11):
        print(i, flush=True)
        time.sleep(1)

def print_letters():
    for letter in 'abcdefghij':
        print(letter, flush=True)
        time.sleep(1)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Оба потока завершены")
