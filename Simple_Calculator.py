# Simple Calculator
def calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get user input
    operation = input("Enter the operation (+, -, *, /): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform calculation based on the operation
    if operation == "+":
        print(f"The result is: {num1 + num2}")
    elif operation == "-":
        print(f"The result is: {num1 - num2}")
    elif operation == "*":
        print(f"The result is: {num1 * num2}")
    elif operation == "/":
        if num2 != 0:  # Avoid division by zero
            print(f"The result is: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please choose +, -, *, or /.")

# Run the calculator
calculator()
