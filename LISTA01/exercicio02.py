
"""Conversão de temperatura de Celsius para Fahrenheit"""
grausCelsius = float(input('Digite a temperatura em graus Celsius: '))
grausFahrenheit = (grausCelsius * 9/5) + 32
grausKelvin = grausCelsius + 273.15
print(f'A temperatura em graus Fahrenheit é: {grausFahrenheit}°F')
print(f'A temperatura em graus Kelvin é: {grausKelvin}K')