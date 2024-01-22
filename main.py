print("Task date: 13.12.2023")
print("Task: 3")

"""
До вже реалізованого класу «Стадіон» додайте можливість
стиснення та розпакування даних з використанням json та
pickle.
"""

import json
import pickle

class Stadium:
    def __init__(self, name, capacity, location):
        self.name = name
        self.capacity = capacity
        self.location = location

    def compress_json(self, filename):
        with open(filename, 'w') as file:
            json.dump({'name': self.name, 'capacity': self.capacity, 'location': self.location}, file)

    def decompress_json(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.name = data['name']
            self.capacity = data['capacity']
            self.location = data['location']

    def compress_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump({'name': self.name, 'capacity': self.capacity, 'location': self.location}, file)

    def decompress_pickle(self, filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            self.name = data['name']
            self.capacity = data['capacity']
            self.location = data['location']