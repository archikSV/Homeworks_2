print("Task date: 22.11.2023")
print("Task: 1")

"""
 Метаклас, який вносить додаткові перевірки/логіку
до певних методів у всіх класах.
"""

class MyMeta(type):
    def __new__(cls, name, bases, dct):
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass