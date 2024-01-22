print("Task date: 13.11.2023")
print("Task: 1")

"""
Створіть клас Device, який містить інформацію про пристрій.
За допомогою механізму успадкування реалізуйте клас
Coffee Machine (містить інформацію про кавомашину), клас
Blender (містить інформацію про блендер), клас MeatGrinder
(містить інформацію про м’ясорубку).
Кожен із класів має містити необхідні для роботи методи.
"""

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class CoffeeMachine(Device):
    def __init__(self, brand, model, coffee_type):
        super().__init__(brand, model)
        self.coffee_type = coffee_type

class Blender(Device):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

class MeatGrinder(Device):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity