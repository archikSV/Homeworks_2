print("Task date: 29.11.2023")
print("Task: 2")

"""
Змініть стек із першого завдання таким чином, щоб його
розмір був нефіксованим.
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return None
        else:
            return self.stack.pop()

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return None
        else:
            return self.stack[-1]