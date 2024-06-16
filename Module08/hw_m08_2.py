from colorama import Fore, Back, Style, init
init(autoreset=True)
class InvalidDataException(Exception):
    """Исключение для недопустимых данных"""
    pass

class ProcessingException(Exception):
    """Исключение для ошибок обработки"""
    pass


def process_data(data):
    if not isinstance(data, int):
        raise InvalidDataException(f"Недопустимый тип данных: {type(data)}. Ожидалось целое число.")
    if data < 0:
        raise ProcessingException("Данные не могут быть отрицательными.")
    return data * 2


def handle_data(data):
    try:
        result = process_data(data)
        print(f"Результат обработки данных: {result}")
    except InvalidDataException as e:
        print(Fore.RED + f"Ошибка: {e}")
        raise
    except ProcessingException as e:
        print(Fore.YELLOW + f"Внимание: {e}")


data_samples = ["строка", -10, 5, -3.14159, {5: 6, 7: 8}, True, [10, 11, -12], (1, 1)]
for data in data_samples:
    try:
        handle_data(data)
    except Exception as e:
        print(Fore.BLUE + f"Исключение передано выше по стеку: {e}")


