print("Task date: 13.11.2023")
print("Task: 2")

"""
Створіть клас Ship, який містить інформацію про кораблі.
За допомогою механізму успадкування реалізуйте клас
Frigate (містить інформацію про фрегат), клас Destroyer(містить
інформацію про есмінця), клас Cruiser (містить інформацію
про крейсер).
Кожен із класів має містити необхідні для роботи методи
"""

class Ship:
    def __init__(self, name, displacement, length):
        self.name = name
        self.displacement = displacement
        self.length = length

class Frigate(Ship):
    def __init__(self, name, displacement, length, num_missiles):
        super().__init__(name, displacement, length)
        self.num_missiles = num_missiles

class Destroyer(Ship):
    def __init__(self, name, displacement, length, num_cannons):
        super().__init__(name, displacement, length)
        self.num_cannons = num_cannons

class Cruiser(Ship):
    def __init__(self, name, displacement, length, num_aircraft):
        super().__init__(name, displacement, length)
        self.num_aircraft = num_aircraft