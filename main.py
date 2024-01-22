print("Task date: 20.11.2023")
print("Task: 1")

"""
Іноді ви можете використати property() для створення
доступу до атрибутів через геттери та сеттери для
забезпечення певних перевірок або операцій перед
отриманням або зміною атрибутів. Створіть клас для
роботи з банківським рахунком, щоб гроші знялися або
зарахувалися тільки при виконанні певних умов
(наприклад, якщо гроші на рахунку є).
"""

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Error: Cannot set negative balance")

    balance = property(get_balance, set_balance)


# Create a BankAccount instance with an initial balance of 100
account = BankAccount(100)

# Get the current balance
print(account.balance)

# Try to set a negative balance
account.balance = -50

# Set a positive balance
account.balance = 150

# Get the updated balance
print(account.balance)