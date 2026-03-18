# This program allows the user to convert between different units of distance, weight, temperature, and volume.
# The user can select a category and then select a specific conversion within that category.
# The program will then prompt the user to enter a value to convert and will display the result of the conversion.

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def km_to_feet(km):
    return km * 3280.84

def feet_to_km(feet):
    return feet / 3280.84

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def g_to_ounces(g):
    return g * 0.035274

def ounces_to_g(ounces):
    return ounces / 0.035274

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons / 0.264172

def liters_to_teaspoons(liters):
    return liters * 202.884

def teaspoons_to_liters(teaspoons):
    return teaspoons / 202.884

menu = {
    'categories': {
        '1': "Distance",
        '2': "Weight",
        '3': "Temperature",
        '4': "Volume",
        '5': "Exit"
    },
    'accepted_inputs': ['1', '2', '3', '4', '5']
}

conversions = {
    'distance': {
        'a': ('Kilometers', 'Miles', km_to_miles),
        'b': ('Miles', 'Kilometers', miles_to_km),
        'c': ('Kilometers', 'Feet', km_to_feet),
        'd': ('Feet', 'Kilometers', feet_to_km)
    },
    'weight': {
        'a': ('Kilograms', 'Pounds', kg_to_pounds),
        'b': ('Pounds', 'Kilograms', pounds_to_kg),
        'c': ('Grams', 'Ounces', g_to_ounces),
        'd': ('Ounces', 'Grams', ounces_to_g)
    },
    'temperature': {
        'a': ('Celsius', 'Fahrenheit', celsius_to_fahrenheit),
        'b': ('Fahrenheit', 'Celsius', fahrenheit_to_celsius),
        'c': ('Celsius', 'Kelvin', celsius_to_kelvin),
        'd': ('Kelvin', 'Celsius', kelvin_to_celsius)
    },
    'volume': {
        'a': ('Liters', 'Gallons', liters_to_gallons),
        'b': ('Gallons', 'Liters', gallons_to_liters),
        'c': ('Liters', 'Teaspoons', liters_to_teaspoons),
        'd': ('Teaspoons', 'Liters', teaspoons_to_liters)
    }
}

clear_screen()

print("Welcome to the Unit Converter!\n")

while True:

    for key, value in menu['categories'].items():
        print(f"{key}. {value}")

    category_choice = input("\nPlease select a category (1-5): ")

    while category_choice not in menu['accepted_inputs']:
        print("\nInvalid input. Please try again.")
        category_choice = input("\nEnter your operation of choice: ")

    if category_choice == '5':
        print("\nThank you for using the Unit Converter. Goodbye!\n")
        break

    number_to_category = {
        '1': 'distance',
        '2': 'weight',
        '3': 'temperature',
        '4': 'volume'
    }

    clear_screen()

    print(f'You have selected {menu['categories'][category_choice]}. These are the options:\n')

    category_choice = number_to_category.get(category_choice, category_choice)
    
    for key, value in conversions[category_choice].items():
        print(f"{key}. {value[0]} to {value[1]}")
    
    conversion_choice = input("\nPlease select a conversion: ")

    while conversion_choice not in conversions[category_choice]:
        print("\nInvalid input. Please try again.")
        conversion_choice = input("\nEnter your conversion of choice: ")

    original_unit = conversions[category_choice][conversion_choice][0]
    conversion_unit = conversions[category_choice][conversion_choice][1]

    clear_screen()

    while True:
        try:
            value_to_convert = float(input(f"\nEnter the value of {original_unit} to convert to {conversion_unit}: "))
            break
        except ValueError:
            print("\nInvalid input. Please enter a number: ")

    conversion_function = conversions[category_choice][conversion_choice][2]

    result = conversion_function(value_to_convert)

    clear_screen()

    print(f'{value_to_convert} {original_unit} is equal to {result:.2f} {conversion_unit}.\n')
