# Celsius to Fahrenheit and back
# Author: Thomas Preston

print('Welcome to temperature conversion.\n')

def Menu():
    print('[1] Convert Celsius to Fahrenheit\n[2] Convert Fahrenheit to Cesius\n[q] Quit\n')
    return input('Select an option from the list.\n')

def GetFloatInput(message):
    return float(input(message))

def ConvertCelsius():
    celsius = GetFloatInput('Enter Celsius Value: ')
    answer = (celsius*9/5) + 32
    rounded = round(answer, 1)
    print(str(celsius) + '°C is',str(rounded) + '°F')

def ConvertFahrenheit():
    fahrenheit = GetFloatInput('Enter Fahrenheit Value: ')
    answer = (fahrenheit - 32) * 5/9
    rounded = round(answer, 1)
    print(str(fahrenheit) + '°F is',str(rounded) + '°C')

while True:
    option = Menu()
    if option == '1':
        ConvertCelsius()
    elif option == '2':
        ConvertFahrenheit()
    elif option == 'q' or option == 'Q':
        exit()
    else:
        print('Invalid option')
