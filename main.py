print("Task date: 11.12.2023")
print("Task: 2")

"""
Маємо певний словник з назвами музичних груп (виконавців) та альбомів. Назва групи використовується як ключ,
назва альбомів — як значення. Реалізуйте: додавання, видалення, пошук, редагування, збереження та завантаження
даних (використовуючи стиснення та розпакування).
"""

class MusicLibrary:
    def __init__(self):
        self.data = {}

    def add_group_album(self, group, album):
        self.data[group] = album

    def remove_group_album(self, group):
        del self.data[group]

    def search_album_by_group(self, group):
        return self.data.get(group)

    def edit_group_album(self, group, new_album):
        if group in self.data:
            self.data[group] = new_album

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



# Create an instance of the MusicLibrary class
ml = MusicLibrary()

# Add music group-album pairs
ml.add_group_album('The Beatles', 'Abbey Road')
ml.add_group_album('Led Zeppelin', 'IV')
ml.add_group_album('Pink Floyd', 'The Dark Side of the Moon')

# Search for an album
print(ml.search_album_by_group('The Beatles'))  # Output: Abbey Road

# Edit a group's album
ml.edit_group_album('The Beatles', 'Sgt. Pepper\'s Lonely Hearts Club Band')
print(ml.search_album_by_group('The Beatles'))  # Output: Sgt. Pepper's Lonely Hearts Club Band

# Save data to a file
ml.save_data('music_library.json')

# Load data from the file
ml.load_data('music_library.json')

# Compress data
ml.compress_data('music_library.json', 'music_library.json.gz')

# Decompress data
ml.decompress_data('music_library.json.gz', 'decompressed_music_library.json')