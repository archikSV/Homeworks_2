print("Task date: 18.12.2023")
print("Task: 2")

"""
Користувач вводить з клавіатури шлях до файлу. Після
чого запускаються три потоки. Перший потік заповнює файл
випадковими числами. Два інші потоки очікують на заповнення. Коли файл заповнений, обидва потоки стартують.
Перший потік знаходить усі прості числа, другий потік знаходить факторіал кожного числа у файлі. Результати пошуку
кожен потік має записати у новий файл. Виведіть на екран
статистику виконаних операцій.
"""

import threading
import random
import math


def fill_file_with_random_numbers(file_path):
    with open(file_path, 'w') as file:
        for _ in range(10):
            file.write(str(random.randint(1, 100)) + '\n')


def find_prime_numbers(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        numbers = [int(line) for line in file.readlines()]

    prime_numbers = [num for num in numbers if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))]

    with open(output_file_path, 'w') as file:
        file.write('\n'.join(map(str, prime_numbers)))


def calculate_factorial(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        numbers = [int(line) for line in file.readlines()]

    factorials = [math.factorial(num) for num in numbers]

    with open(output_file_path, 'w') as file:
        file.write('\n'.join(map(str, factorials)))


def main():
    file_path = input("Enter the file path: ")
    thread1 = threading.Thread(target=fill_file_with_random_numbers, args=(file_path,))
    thread2 = threading.Thread(target=find_prime_numbers, args=(file_path, 'prime_numbers.txt'))
    thread3 = threading.Thread(target=calculate_factorial, args=(file_path, 'factorials.txt'))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()


if __name__ == "__main__":
    main()