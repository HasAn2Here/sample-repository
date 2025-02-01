# Function to calculate concentration
def calculate_concentration(solute, volume):
    try:
        concentration = solute / volume
        return concentration
    except ZeroDivisionError:
        return "Error: Volume cannot be zero!"

# User inputs
solute = float(input("Enter the amount of solute (in moles): "))
volume = float(input("Enter the volume of the solution (in liters): "))

# Calculate and display the result
result = calculate_concentration(solute, volume)
if isinstance(result, str):
    print(result)  # Print error message if volume is zero
else:
    print(f"The concentration of the solution is {result:.2f} mol/L")
