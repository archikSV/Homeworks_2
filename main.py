print("Task date: 3.12.2023")
print("Task: 1")

"""
Розробіть додаток, що імітує чергу запитів до сервера.
Мають бути клієнти, які надсилають запити на сервер, кожен
з яких має свій пріоритет. Кожен новий клієнт потрапляє у
чергу залежно від свого пріоритету. Зберігайте статистику
запитів (користувач, час) в окремій черзі.
Передбачте виведення статистики на екран. Вибір необхідних структур даних визначте самостійно.
"""

from queue import PriorityQueue
import time

class Request:
    def __init__(self, user, time):
        self.user = user
        self.time = time

    def __lt__(self, other):
        return self.time < other.time

class Server:
    def __init__(self):
        self.request_queue = PriorityQueue()

    def handle_request(self, user, priority):
        request = Request(user, time.time())
        self.request_queue.put((priority, request))

    def show_statistics(self):
        while not self.request_queue.empty():
            priority, request = self.request_queue.get()
            print(f"User: {request.user}, Time: {request.time}")

# Usage
server = Server()
server.handle_request("User1", 3)
server.handle_request("User2", 1)
server.handle_request("User3", 2)
server.show_statistics()