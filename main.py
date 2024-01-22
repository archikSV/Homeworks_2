print("Task date: 22.11.2023")
print("Task: 2")

"""
Метаклас, що може змінювати ім'я класу залежно
від певних умов або параметрів.
"""

class DynamicClassName(type):
    def __new__(cls, name, bases, dct):
       return super().__new__(cls, name, bases, dct)