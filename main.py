print("Task date: 11.12.2023")
print("Task: 1")

"""
Маємо певний словник з назвами країн і столиць. Назва
країни використовується як ключ, назва столиці — як значення. Реалізуйте: додавання, видалення, пошук, редагування,
збереження та завантаження даних (використовуючи стиснення та розпакування).
"""

class CountryCapitals:
    def __init__(self):
        self.data = {}

    def add_country_capital(self, country, capital):
        self.data[country] = capital

    def remove_country_capital(self, country):
        del self.data[country]

    def search_capital_by_country(self, country):
        return self.data.get(country)

    def edit_country_capital(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital

    def save_data(self, file_name):
        import json
        with open(file_name, 'w') as file:
            json.dump(self.data, file)

    def load_data(self, file_name):
        import json
        with open(file_name, 'r') as file:
            self.data = json.load(file)

    def compress_data(self, file_name, compressed_file_name):
        import gzip
        with open(file_name, 'rb') as file:
            with gzip.open(compressed_file_name, 'wb') as compressed_file:
                compressed_file.writelines(file)

    def decompress_data(self, compressed_file_name, decompressed_file_name):
        import gzip
        with gzip.open(compressed_file_name, 'rb') as compressed_file:
            with open(decompressed_file_name, 'wb') as decompressed_file:
                decompressed_file.writelines(compressed_file)


# Create an instance of the CountryCapitals class
cc = CountryCapitals()

# Add country-capital pairs
cc.add_country_capital('USA', 'Washington D.C.')
cc.add_country_capital('Canada', 'Ottawa')
cc.add_country_capital('France', 'Paris')

# Search for a capital
print(cc.search_capital_by_country('USA'))  # Output: Washington D.C.

# Edit a country's capital
cc.edit_country_capital('USA', 'New York')
print(cc.search_capital_by_country('USA'))  # Output: New York

# Save data to a file
cc.save_data('country_capitals.json')

# Load data from the file
cc.load_data('country_capitals.json')

# Compress data
cc.compress_data('country_capitals.json', 'country_capitals.json.gz')

# Decompress data
cc.decompress_data('country_capitals.json.gz', 'decompressed_country_capitals.json')