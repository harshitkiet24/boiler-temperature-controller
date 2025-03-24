
def check_boiler_temp(temp):
    if temp <= 10:
        print("Temperature is too low. Consider preheating the boiler.")
    elif temp > 35:
        print("Temperature is too high. Cooling system needs to be activated.")
    elif 10 < temp < 20:
        print("Temperature is slightly below optimal. Adjust settings.")
    elif 20 <= temp <= 30:
        print("Temperature is in the safe zone.")
    elif 30 < temp <= 35:
        print("Temperature is slightly above optimal. Monitor closely.")
    else:
        print("Error: Invalid temperature input.")

def convert_temperature(temp, to_scale):
    if to_scale.lower() == "f":
        return (temp * 9/5) + 32  # Celsius to Fahrenheit
    elif to_scale.lower() == "c":
        return (temp - 32) * 5/9  # Fahrenheit to Celsius
    else:
        return None

try:
    print("Choose an option:")
    print("1. Check boiler temperature")
    print("2. Convert temperature")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        temp = float(input("Enter the temperature in Celsius: "))
        check_boiler_temp(temp)
    elif choice == 2:
        temp = float(input("Enter the temperature: "))
        scale = input("Convert to (C for Celsius, F for Fahrenheit): ")
        converted_temp = convert_temperature(temp, scale)
        if converted_temp is not None:
            print(f"The converted temperature is: {converted_temp:.2f}°{scale.upper()}")
        else:
            print("Invalid scale input! Please choose 'C' or 'F'.")
    else:
        print("Invalid choice! Please select 1 or 2.")
except ValueError:
    print("Invalid input! Please enter numeric values where required.")
