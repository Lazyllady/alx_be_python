# temp_conversion_tool.py

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit: float):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

if __name__ == "__main__":
    raw = input("Enter the temperature to convert: ").strip()
    try:
        temp = float(raw)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == 'F':
        converted = convert_to_celsius(temp)
        print(f"{temp}°F is {converted}°C")
    elif unit == 'C':
        converted = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted}°F")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")
