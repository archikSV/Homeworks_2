print("Task date: 22.11.2023")
print("Task: 3")

"""
Створіть метаклас, який автоматично додає певні
атрибути до всіх класів, що використовують його
"""

class AutoAttributeAdder(type):
    def __new__(cls, name, bases, dct):
        dct['added_attribute'] = 'This attribute was added automatically'
        return super().__new__(cls, name, bases, dct)