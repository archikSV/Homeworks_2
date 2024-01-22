print("Task date: 22.11.2023")
print("Task: 4")

"""
Метаклас, що додає перевірку та обробку аргументів
__init__ у всіх класах.
"""

class ArgumentCheckerMeta(type):
    def __init__(cls, name, bases, dct):
        original_init = cls.__init__

        def new_init(self, *args, **kwargs):
            print("Argument checking and processing logic here")
            original_init(self, *args, **kwargs)

        cls.__init__ = new_init
        super().__init__(name, bases, dct)