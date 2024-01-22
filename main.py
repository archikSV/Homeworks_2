print("Task date: 20.11.2023")
print("Task: 2")

"""
Створіть клас температурного датчика, де обмежується
температура в межах прийнятних для датчика значень, за
допомогою property().
"""

class TemperatureSensor:
    def __init__(self, temperature):
        self._temperature = temperature

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, new_temperature):
        if -50 <= new_temperature <= 50:  # Example acceptable temperature range
            self._temperature = new_temperature
        else:
            print("Error: Temperature out of acceptable range")

    temperature = property(get_temperature, set_temperature)



# Create a TemperatureSensor instance with an initial temperature of 25
sensor = TemperatureSensor(25)

# Get the current temperature
print(sensor.temperature)

# Try to set a temperature outside the acceptable range
sensor.temperature = 60

# Set a temperature within the acceptable range
sensor.temperature = 10

# Get the updated temperature
print(sensor.temperature)