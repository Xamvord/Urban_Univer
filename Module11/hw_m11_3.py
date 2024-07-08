import inspect

def introspection_info(obj):
    obj_type = type(obj)
    attributes = dir(obj)

    methods = [attr for attr in attributes if callable(getattr(obj, attr))]
    non_methods = [attr for attr in attributes if not callable(getattr(obj, attr))]

    module = inspect.getmodule(obj)
    module_name = module.__name__ if module else None

    info = {
        'type': obj_type.__name__,
        'attributes': non_methods,
        'methods': methods,
        'module': module_name
    }

    return info

class MySuperClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def my_supermethod(self):
        return self.x * self.y

my_superobject = MySuperClass(6, 7)
# print(my_superobject.my_supermethod())

# =================================================================== #

# Пример 1: Число
number_info = introspection_info(42)
print(number_info)

# Пример 2: Строка
string_info = introspection_info("hello")
print(string_info)

# Пример 3: Список
list_info = introspection_info([1, 2, 3])
print(list_info)

# Пример 4: Пользовательский класс
class_info = introspection_info(MySuperClass)
print(class_info)

# Пример 5: Объект пользовательского класса
object_info = introspection_info(my_superobject)
print(object_info)

