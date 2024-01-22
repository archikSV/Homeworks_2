print("Homework date: 15.11.2023")

"""
Task 1:
Створіть базовий клас «Фігура» з методом для підрахунку
площі. Створіть похідні класи: прямокутник, коло, прямокутний трикутник, трапеція, зі своїми методами для підрахунку
площі. 

Task 2:
Для класів із першого завдання перевизначте магічні
методи int (повертає площу) та str (повертає інформацію
про фігуру).

Task 3:
Створіть базовий клас Shape для рисування плоских фігур. Визначте методи:
■ Show() — виведення на екран інформації про фігуру;
■ Save() — збереження фігури у файл;
■ Load() — зчитування фігури з файлу.
Визначте похідні класи:
■ Square — квадрат із заданими з координатами лівого
верхнього кута та довжиною сторони.
■ Rectangle — прямокутник із заданими координатами
верхнього лівого кута та розмірами.
■ Circle — коло із заданими координатами центру та радіусом.
■ Ellipse — еліпс із заданими координатами верхнього кута
описаного навколо нього прямокутника зі сторонами,
паралельними осям координат, та розмірами цього прямокутника. 
"""

import math
import json

class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden in a derived class")

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f"{self.__class__.__name__} with area: {self.area()}"

    def show(self):
        raise NotImplementedError("This method should be overridden in a derived class")

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

    def load(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        for key, value in data.items():
            setattr(self, key, value)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def show(self):
        return f"Rectangle with width: {self.width}, height: {self.height}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def show(self):
        return f"Circle with radius: {self.radius}"

    def load(self, filename):
        super().load(filename)
        self.radius = float(self.radius)  # Ensure radius is a float

class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def show(self):
        return f"RightTriangle with base: {self.base}, height: {self.height}"

class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def show(self):
        return f"Trapezoid with bases: {self.base1}, {self.base2} and height: {self.height}"

class Square(Shape):
    def __init__(self, top_left, side_length):
        self.top_left = top_left
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def show(self):
        return f"Square with top left corner at {self.top_left} and side length {self.side_length}"

class Ellipse(Shape):
    def __init__(self, top_left, width, height):
        self.top_left = top_left
        self.width = width
        self.height = height

    def area(self):
        return math.pi * (self.width / 2) * (self.height / 2)

    def show(self):
        return f"Ellipse with top left corner at {self.top_left}, width {self.width}, height {self.height}"


# Демонстрація роботи класів
# Створення об'єктів різних фігур
rectangle = Rectangle(10, 5)
circle = Circle(3)
right_triangle = RightTriangle(4, 6)
trapezoid = Trapezoid(3, 4, 5)
square = Square((0, 0), 4)
ellipse = Ellipse((1, 1), 6, 3)

# Демонстрація площі та інформації про кожну фігуру
figures = [rectangle, circle, right_triangle, trapezoid, square, ellipse]

for figure in figures:
    print(figure)
    print(figure.show())
    print('-' * 30)

# Збереження та завантаження фігур
filename = "shape_data.json"

# Збереження
for figure in figures:
    figure.save(filename)
    print(f"Saved {figure} to {filename}")

# Завантаження
for figure in figures:
    figure.load(filename)
    print(f"Loaded {figure} from {filename}")
