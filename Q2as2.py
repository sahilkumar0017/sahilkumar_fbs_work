# Python program to convert Celsius to Fahrenheit
# Formula: C/5 = (F - 32)/9

    # Take Celsius input from user
celsius = float(input("Enter temperature in Celsius: "))

    # Apply the formula to convert Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

    # Display the result
print(f"{celsius}°C is equal to {fahrenheit}°F")