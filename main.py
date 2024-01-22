print("Task date: 18.12.2023")
print("Task: 4")

"""
Користувач вводить з клавіатури шлях до існуючої директорії та слово для пошуку. Після чого запускаються два
потоки. Перший потік має знайти файли з потрібним словом
і злити їх вміст в один файл. Другий потік очікує на завершення роботи першого потоку і проводить виключення усіх
заборонених слів (список цих слів потрібно зчитати з файлу
із забороненими словами) з отриманого файлу. Виведіть статистику виконаних операцій на екран.
"""

import threading
import os

def search_and_merge(directory, search_word, output_file):
    files_with_search_word = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            with open(os.path.join(root, file), 'r') as f:
                content = f.read()
                if search_word in content:
                    files_with_search_word.append(os.path.join(root, file))

    with open(output_file, 'w') as out_file:
        for file in files_with_search_word:
            with open(file, 'r') as f:
                out_file.write(f.read())

def exclude_words(input_file, banned_words_file, output_file):
    with open(banned_words_file, 'r') as f:
        banned_words = set(f.read().split())

    with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
        for line in input_f:
            words = line.split()
            filtered_words = [word for word in words if word.lower() not in banned_words]
            output_f.write(" ".join(filtered_words) + "\n")

def main():
    source_dir = input("Enter the path to the existing directory: ")
    search_word = input("Enter the word to search for: ")
    banned_words_file = "banned_words.txt"
    output_file = "merged_content.txt"
    final_output_file = "final_output.txt"

    t1 = threading.Thread(target=search_and_merge, args=(source_dir, search_word, output_file))
    t2 = threading.Thread(target=exclude_words, args=(output_file, banned_words_file, final_output_file))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Operations completed.")

if __name__ == "__main__":
    main()