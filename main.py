print("Task date: 29.11.2023")
print("Task: 1")

"""
Реалізуйте клас стеку для роботи з рядками (стек рядків).
Стек має бути фіксованого розміру. Реалізуйте набір операцій
для роботи зі стеком:
o розміщення рядка у стек;
o виштовхування рядка зі стеку;
o підрахунок кількості рядків у стеку;
o перевірку, чи порожній стек;
o перевірку, чи повний стек;
o очищення стеку;
o отримання значення без виштовхування
верхнього рядка зі стеку.
На старті додатка відобразіть меню, в якому користувач
може вибрати необхідну операцію
"""

class FixedSizeStack:
    def __init__(self, size):
        self.stack = [None] * size
        self.size = size
        self.top = -1

    def push(self, item):
        if self.top == self.size - 1:
            print("Stack is full")
        else:
            self.top += 1
            self.stack[self.top] = item

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            item = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return item

    def count(self):
        return self.top + 1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def clear(self):
        self.stack = [None] * self.size
        self.top = -1

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            return self.stack[self.top]