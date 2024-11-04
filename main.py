# Example 1

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    """This function takes a temperature in Celsius and converts it to Fahrenheit."""
    # The formula to convert Celsius to Fahrenheit
    return (celsius * 9 / 5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    # The formula to convert Fahrenheit to Celsius
    return (fahrenheit - 32) * 5 / 9

def main():
    # Welcome message for the user
    print("Welcome to the Temperature Converter!")

    # Step 2: Get User Input
    print("Choose the conversion type:")
    print("1: Convert Celsius to Fahrenheit")
    print("2: Convert Fahrenheit to Celsius")

    conversion_type = input("Enter 1 or 2: ")  

    # Check if the user wants to convert Celsius to Fahrenheit
    if conversion_type == '1':
        celsius = float(input("Please enter the temperature in Celsius: "))  
        converted_temp = celsius_to_fahrenheit(celsius)  
        print(f"{celsius:.2f} °C is equal to {converted_temp:.2f} °F")  

    # Check if the user wants to convert Fahrenheit to Celsius
    elif conversion_type == '2':
        fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))  
        converted_temp = fahrenheit_to_celsius(fahrenheit)  
        print(f"{fahrenheit:.2f} °F is equal to {converted_temp:.2f} °C")  

    # If the input is not valid
    else:
        print("Invalid option selected. Please choose either 1 or 2.") 






# Nashville's example

# Step 1: Define conversion functions

# Celsius to Fahrenheit conversion
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Fahrenheit to Celsius conversion
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Step 2: Get user input for the conversion type
print("Welcome to the Temperature Converter!")
print("Choose the type of conversion:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter 1 or 2: ")

# Step 3: Get the temperature to convert based on the user's choice
if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    # Step 4: Perform the conversion and display the result
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    # Step 4: Perform the conversion and display the result
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
    print("Invalid choice. Please enter 1 or 2.")
