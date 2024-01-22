print("Task date: 13.12.2023")
print("Task: 1")

"""
Створіть два окремих "мікросервіси" (дві окремі
програми). Одна програма створює та експортує дані у
форматі JSON, а інша програма завантажує та обробляє ці
дані. Це може бути, наприклад, система, яка створює та
обробляє замовлення.
"""

# Service 1: Export data in JSON format
import json

data = {
    "order_id": 12345,
    "product": "Smartphone",
    "quantity": 2
}

with open('data.json', 'w') as file:
    json.dump(data, file)


# Service 2: Load and process the data
import json

with open('data.json', 'r') as file:
    data = json.load(file)
    print("Order ID:", data['order_id'])
    print("Product:", data['product'])
    print("Quantity:", data['quantity'])