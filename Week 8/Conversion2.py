# Celsius to Fahrenheit and back (version 2) using classes
# Author: Thomas Preston

class TempConverter: 
    def CelsiusToFahrenheit(self, celsius):
        return (celsius*9/5) + 32
    def FahrenheitToCelsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

class TempInterface:
    def __init__(self, converter):
        self.converter = converter
    def GetFloatInput(self, message):
        return float(input(message))
    def ConvertCelsius(self):
        celsius = self.GetFloatInput('Enter Celsius Value: ')
        answer = self.converter.CelsiusToFahrenheit(celsius)
        rounded = round(answer, 1)
        print(str(celsius) + '°C is',str(rounded) + '°F')
    def ConvertFahrenheit(self):
        fahrenheit = self.GetFloatInput('Enter Fahrenheit Value: ')
        answer = self.converter.FahrenheitToCelsius(fahrenheit)
        rounded = round(answer, 1)
        print(str(fahrenheit) + '°F is',str(rounded) + '°C')

class Convertion:
    def __init__(self):
        self.tempInterface = TempInterface(TempConverter()) 
    def Menu(self):
        print('[1] Convert Celsius to Fahrenheit\n[2] Convert Fahrenheit to Cesius\n[q] Quit\n')
        return input('Select an option from the list.\n')
    def run(self):
        print('Welcome to temperature conversion.\n')
        while True:
            option = self.Menu()
            if option == '1':
                self.tempInterface.ConvertCelsius()
            elif option == '2':
                self.tempInterface.ConvertFahrenheit()
            elif option == 'q' or option == 'Q':
                exit()
            else:
                print('Invalid option')

Convertion().run()