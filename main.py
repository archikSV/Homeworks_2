print("Task date: 6.12.2023")
print("Task: 1")

"""
Реалізуйте базу даних зі штрафами податкової
інспекції. Ідентифікувати кожну конкретну людину буде
персональний ідентифікаційний код. В однієї людини може
бути багато штрафів.
Реалізуйте:
1. Повний друк бази даних;
2. Друк даних за конкретним кодом;
3. Друк даних за конкретним типом штрафу;
4. Друк даних за конкретним містом;
5. Додавання нової людини з інформацією про неї;
6. Додавання нових штрафів для вже існуючого запису;
7. Видалення штрафу;
8. Заміна інформації про людину та її штрафи.
Використайте дерево для реалізації цього завдання.
"""

class TaxInspectionDatabase:
    def __init__(self):
        self.database = {}

    def print_full_database(self):
        for code, fines in self.database.items():
            print(f"Code: {code}")
            for fine in fines:
                print(fine)
            print()

    def print_data_by_code(self, code):
        if code in self.database:
            print(f"Code: {code}")
            for fine in self.database[code]:
                print(fine)
        else:
            print("No data found for the specified code.")

    def print_data_by_fine_type(self, fine_type):
        for code, fines in self.database.items():
            for fine in fines:
                if fine.get('type') == fine_type:
                    print(f"Code: {code}")
                    print(fine)

    def print_data_by_city(self, city):
        for code, fines in self.database.items():
            for fine in fines:
                if fine.get('city') == city:
                    print(f"Code: {code}")
                    print(fine)

    def add_person(self, code, person_info):
        if code not in self.database:
            self.database[code] = []
        self.database[code].append(person_info)

    def add_fine(self, code, new_fine):
        if code in self.database:
            self.database[code].append(new_fine)
        else:
            print("Person not found in the database.")

    def remove_fine(self, code, fine_to_remove):
        if code in self.database:
            if fine_to_remove in self.database[code]:
                self.database[code].remove(fine_to_remove)
            else:
                print("Fine not found for the specified person.")
        else:
            print("Person not found in the database.")

    def update_person_info(self, code, updated_info):
        if code in self.database:
            self.database[code] = updated_info
        else:
            print("Person not found in the database.")

# Example usage:
database = TaxInspectionDatabase()
person1_info = {
    'name': 'John Doe',
    'city': 'New York'
}
person2_info = {
    'name': 'Jane Smith',
    'city': 'Los Angeles'
}
fine1 = {
    'type': 'Speeding',
    'amount': 100
}
fine2 = {
    'type': 'Parking violation',
    'amount': 50
}
database.add_person('12345', person1_info)
database.add_fine('12345', fine1)
database.add_person('67890', person2_info)
database.add_fine('67890', fine2)

database.print_full_database()
database.print_data_by_code('12345')
database.print_data_by_fine_type('Speeding')
database.print_data_by_city('New York')
