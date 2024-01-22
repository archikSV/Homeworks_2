print("Task date: 18.12.2023")
print("Task: 1")

"""
При старті додатку запускаються три потоки. Перший
потік заповнює список випадковими числами. Два інші потоки
очікують на заповнення. Коли перелік заповнений, обидва
потоки запускаються. Перший потік знаходить суму елементів
списку, другий потік знаходить середнє арифметичне значення
у списку. Отриманий список, сума та середнє арифметичне
виводяться на екран. 
"""

import threading
import random

# Функція для заповнення списку випадковими числами
def fill_list(lst):
    for _ in range(10):
        lst.append(random.randint(1, 100))

# Функція для знаходження суми елементів списку
def calculate_sum(lst):
    total_sum = sum(lst)
    print(f"Сума елементів списку: {total_sum}")

# Функція для знаходження середнього арифметичного значення у списку
def calculate_average(lst):
    avg = sum(lst) / len(lst)
    print(f"Середнє арифметичне значення у списку: {avg}")

# Створення пустого списку
my_list = []

# Створення потоків
thread1 = threading.Thread(target=fill_list, args=(my_list,))
thread2 = threading.Thread(target=calculate_sum, args=(my_list,))
thread3 = threading.Thread(target=calculate_average, args=(my_list,))

# Запуск першого потоку для заповнення списку
thread1.start()

# Очікування завершення заповнення списку
thread1.join()

# Запуск двох інших потоків
thread2.start()
thread3.start()

# Очікування завершення обох потоків
thread2.join()
thread3.join()