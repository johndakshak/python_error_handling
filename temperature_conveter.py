# ===== TASK 3: Temperature Converter =====
# Create a custom TemperatureError exception
# The function should convert Celsius to Fahrenheit and raise TemperatureError if:
# - Temperature is below absolute zero (-273.15°C)
# - Temperature is above the surface of the sun (5500°C)
# If input is not a number, raise ValueError with message "Error: invalid temperature"
# Keep asking until a valid temperature is entered

print("=== Task 3: Temperature Converter ===")
print("Enter temperature in Celsius (must be between -273.15°C and 5500°C)\n")

class TemperatureError(Exception):
    pass

def convert_temperature(prompt):
    #
    # Write your code here.
    # Define TemperatureError class
    # Convert input to float
    # Validate temperature range
    # Calculate Fahrenheit: (celsius * 9/5) + 32
    # Handle exceptions and keep prompting
    #
    
    flag = True

    while flag:
        try:
            celsius = float(input(prompt))

            if celsius < -273.15:
                raise TemperatureError("Error: temperature cannot be below absolute zero (-273.15°C)")
            
            elif celsius > 5500:
                raise TemperatureError("Error: temperature cannot exceed surface of the sun (5500°C)")

            flag = False
            return celsius

        except ValueError:
            print("Error: invalid temperature (must be a number)")
        except TemperatureError as temperature_error:
            print(temperature_error)

celsius = convert_temperature("Enter temperature in Celsius: ")
fahrenheit = (float(celsius) * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
print()
