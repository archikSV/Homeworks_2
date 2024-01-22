print("Task date: 13.12.2023")
print("Task: 2")

"""
Створіть програму для проведення опитування або
анкетування. Зберігайте відповіді користувачів у форматі
JSON файлу. Кожне опитування може бути окремим
об'єктом у файлі JSON, а відповіді кожного користувача -
списком значень.
"""

import json

# Get responses from the user
responses = []

while True:
    response = input("Please enter your response (or 'q' to quit): ")
    if response == 'q':
        break
    responses.append(response)

# Save responses to a JSON file
with open('survey_responses.json', 'w') as file:
    json.dump(responses, file)