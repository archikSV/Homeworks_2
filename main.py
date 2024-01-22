print("Task date: 13.11.2023")
print("Task: 3")

"""
Запрограмуйте клас Money (об’єкт класу оперує однією
валютою) для роботи з грошима.
У класі мають бути передбачені: поле для зберігання цілої
частини грошей (долари, євро, гривні тощо) і поле для зберігання копійок (центи, євроценти, копійки тощо).
Реалізуйте методи виведення суми на екран, задання
значень частин.
Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money. Реалізуйте метод для
зменшення ціни на задане число.
Для кожного з класів реалізуйте необхідні методи та поля.
"""

class Money:
    def __init__(self, currency, amount, cents):
        self.currency = currency
        self.amount = amount
        self.cents = cents

    def display_amount(self):
        print(f"{self.amount} {self.currency} and {self.cents} cents")

    def set_amount(self, amount, cents):
        self.amount = amount
        self.cents = cents

class Product(Money):
    def reduce_price(self, amount):
        self.amount -= amount
        if self.amount < 0:
            print("Price cannot be negative")