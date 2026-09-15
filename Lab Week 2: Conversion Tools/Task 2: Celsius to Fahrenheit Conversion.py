fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit_to_celsius = (fahrenheit - 32) * 5/9
celsius_to_fahrenheit = celsius * 9/5 + 32

print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius:.2f}°C.")
print(f"{celsius}°C is equal to {celsius_to_fahrenheit:.2f}°F.")
# same as task 1 i made this code for both ways in conversion.