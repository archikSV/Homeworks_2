print("Task date: 20.11.2023")
print("Task: 2")

"""
 Завдання для функторів. Створіть клас TextModifier,
який може здійснювати різні операції над текстом:
• Операція перетворення тексту у верхній регістр.
• Операція перетворення тексту у нижній регістр.
• Операція видалення пробілів у тексті.
• Операція шифрування тексту за допомогою зсуву
вліво на задану кількість символів.
"""

class TextModifier:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        self.text = self.text.upper()

    def to_lower(self):
        self.text = self.text.lower()

    def remove_spaces(self):
        self.text = self.text.replace(' ', '')

    def encrypt(self, shift):
        encrypted_text = ''
        for char in self.text:
            if char.isalpha():
                shifted_char_code = ord(char) + shift
                if char.islower():
                    if shifted_char_code > ord('z'):
                        shifted_char_code -= 26
                elif char.isupper():
                    if shifted_char_code > ord('Z'):
                        shifted_char_code -= 26
                encrypted_text += chr(shifted_char_code)
            else:
                encrypted_text += char
        self.text = encrypted_text



modifier = TextModifier("Hello, World!")
modifier.to_upper()
print(modifier.text)  # Output: "HELLO, WORLD!"

modifier.to_lower()
print(modifier.text)  # Output: "hello, world!"

modifier.remove_spaces()
print(modifier.text)  # Output: "hello,world!"

modifier.encrypt(3)
print(modifier.text)  # Output: "khoor,zruog!"