print("Task date: 18.12.2023")
print("Task: 3")

"""
Користувач вводить з клавіатури шлях до існуючої та
до нової директорії. Після чого запускається потік, який має
скопіювати вміст директорії у нове місце. Збережіть структуру
директорії. Виведіть статистику виконаних операцій на екран.
"""

import threading
import shutil

def copy_directory_contents(source_dir, dest_dir):
    try:
        shutil.copytree(source_dir, dest_dir)
    except FileExistsError:
        print(f"The directory {dest_dir} already exists.")

source_dir = input("Enter the path to the existing directory: ")
dest_dir = input("Enter the path to the new directory: ")

thread = threading.Thread(target=copy_directory_contents, args=(source_dir, dest_dir))
thread.start()
thread.join()

print("Directory contents copied successfully.")